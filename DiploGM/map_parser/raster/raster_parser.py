import json
import math
import logging
from enum import StrEnum
from typing import Any

import numpy as np
from PIL import Image
from numpy import dtype, ndarray
from scipy import ndimage
from skimage.measure import regionprops
from skimage.measure._regionprops import RegionProperties
from skimage.segmentation import expand_labels, find_boundaries

from DiploGM.map_parser.raster import utils
from DiploGM.models.board import Board
from DiploGM.models.province import Province, ProvinceType

logger = logging.getLogger(__name__)


class Layer(StrEnum):
    BACKGROUND = "background"
    CENTERS = "centers"
    NAMES = "names"
    UNITS = "units"


def parse_variant(variant_directory: str) -> Board:
    """

    Parse variant for raster encoding. (assumes png)
    I originally learned this whole method for parsing map PNGs from looking through felixludos' conda notebooks
    for his digi-diplo project, so credit there. I think the plot_region_info in utils is fully lifted from there,
    but a lot of the rest of this code is what I've learned works well after having reimplemented this same general
    method for different projects over the years.

    Load the layers in as separate images, use labeling methods to break them up into regions, and find
    adjacencies/overlaps to work it into a Board.

    :param variant_directory: File directory name that contains a `config.json` file to point to other layer files.
    :return: Board DiploGM object
    """
    logger.info("Parsing new variant %s", variant_directory)
    config = None
    with open(f"variants/{variant_directory}/config.json", "r") as config_json_file:
        config = json.load(config_json_file)

    background_layer_filename = config["file config"]["background_layer"]
    centers_layer_filename = config["file config"]["centers_layer"]
    names_layer_filename = config["file config"]["names_layer"]
    units_layer_filename = config["file config"]["units_layer"]

    layer_order: list[Layer | str] = [Layer.BACKGROUND, Layer.CENTERS, Layer.NAMES, Layer.UNITS]

    # Insert additional layers backward so two additionals following same layer occur in right order
    for additional_layer_config in reversed(config["file config"]["additional_layers"]):
        file_name = additional_layer_config["name"]
        place_above_layer = Layer(additional_layer_config["place_above"].lower())
        index = layer_order.index(place_above_layer)
        layer_order.insert(index + 1, file_name)

    army_filename = config["file config"]["army_template"]
    fleet_filename = config["file config"]["fleet_template"]

    border_color = utils.hex_string_to_color(config["file config"]["border_color"])
    border_thickness = config["file config"]["border_thickness"]

    background_image = np.asarray(Image.open(f"variants/{variant_directory}/{background_layer_filename}").convert("RGBA"))
    bg_labels, ndlabels = ndimage.label((background_image != border_color).any(-1), structure=np.ones((3, 3)))

    centers_image = np.asarray(Image.open(f"variants/{variant_directory}/{centers_layer_filename}").convert("RGBA"))
    names_image = np.asarray(Image.open(f"variants/{variant_directory}/{names_layer_filename}").convert("RGBA"))
    assert background_image.shape == centers_image.shape and centers_image.shape == names_image.shape, "Input layers not same size"
    image_height, image_width = background_image.shape[:2]

    army_image = np.asarray(Image.open(f"variants/{variant_directory}/{army_filename}").convert("RGBA"))
    fleet_image = np.asarray(Image.open(f"variants/{variant_directory}/{fleet_filename}").convert("RGBA"))
    army_height, army_width = army_image.shape[:2]
    fleet_height, fleet_width = fleet_image.shape[:2]
    assert army_height < image_height and army_width < image_width, "Army too big for map"
    assert fleet_height < image_height and fleet_width < image_width, "Fleet too big for map"

    utils.plot_region_info(bg_labels)

    provinces = [ Province("unknown", None, dict(), dict(), ProvinceType.IMPASSIBLE,
                           False, set(), set(), None, None, None)
                  for _ in range(ndlabels) ]

    expanded_labels = expand_labels(bg_labels, distance=border_thickness)
    army_mask = (army_image[:, :, 3] != 0)
    fleet_mask = (fleet_image[:, :, 3] != 0)
    region_properties = regionprops(bg_labels)
    for index, province in enumerate(provinces):
        props = region_properties[index]
        label = index + 1
        assert props.label == label, "Desync in region properties iteration"

        boundaries = find_boundaries(expanded_labels == label, mode='outer', background=False)
        province.adjacent = { provinces[adjacent_label-1]
                              for adjacent_label
                              in np.setdiff1d(np.unique(expanded_labels[boundaries]),[0], assume_unique=True)
                              }

        determine_unit_coord(bg_labels, centers_image, names_image, army_mask, props)

    return


def determine_unit_coord(bg_labels: ndarray[tuple[int]], centers_image: ndarray[tuple[Any, ...], dtype[Any]],
                         names_image: ndarray[tuple[Any, ...], dtype[Any]], unit_mask: ndarray[tuple[bool]],
                         props: RegionProperties):
    # Initial candidate is the centroid of the region
    unit_coord_y, unit_coord_x = props.centroid
    unit_coord_y, unit_coord_x = int(unit_coord_y), int(unit_coord_x)
    min_y, min_x, max_y, max_x = props.bbox
    region_height, region_width = max_y - min_y, max_x - min_x
    unit_height, unit_width = unit_mask.shape[:2]
    image_height, image_width = bg_labels.shape[:2]

    orientation = props.orientation
    angle_x = -math.sin(orientation)
    angle_y = -math.cos(orientation)

    #Extremely small regions
    if region_height < unit_height and region_width < unit_width:
        bounded_x = np.clip(unit_coord_x, a_min=(unit_width // 2), a_max=image_width - (unit_width // 2) - 1)
        bounded_y = np.clip(unit_coord_y, a_min=(unit_height // 2), a_max=image_height - (unit_height // 2) - 1)
        return bounded_x, bounded_y

    #Extremely narrow regions
    if region_height < unit_height:
        angle_y = 0
        angle_x = math.copysign(1, angle_x)
    elif region_width < unit_width:
        angle_x = 0
        angle_y = math.copysign(1, angle_y)

    # Make sure it's on the map
    top_left_bbox_x = np.clip(unit_coord_x - (unit_width // 2), a_min=0, a_max=image_width - unit_width - 1)
    top_left_bbox_y = np.clip(unit_coord_y - (unit_height // 2), a_min=0, a_max=image_height - unit_height - 1)

    # First, try to fit unit_coord not on top of the centers or names of the region
    uncovered_coords = (bg_labels == props.label) & (names_image[:, :, 3] == 0) & (centers_image[:, :, 3] == 0)

    distance_ray = np.arange(0, int(0.5 * props.axis_major_length))
    y_offsets = (distance_ray * angle_y).astype(int)
    x_offsets = (distance_ray * angle_x).astype(int)
    print(props.label)
    print(y_offsets)
    print(x_offsets)
    valid_coords = (bg_labels[unit_coord_y + y_offsets, unit_coord_x + x_offsets]
                    == props.label)
    print(props.label, valid_coords)
    utils.unit_fit_for_spot(unit_mask, uncovered_coords, (top_left_bbox_x, top_left_bbox_y),
                                      unit_width, unit_height)
