import math

import numpy as np

import matplotlib.pyplot as plt
from skimage.measure import regionprops


def plot_image(image):
    plt.imshow(image)
    plt.show()


def plot_region_info(labels):
    fig, ax = plt.subplots()
    ax.imshow(labels, cmap='gray')
    regions = regionprops(labels)
    for props in regions:
        y0, x0 = props.centroid
        orientation = props.orientation

        x1 = x0 + math.cos(orientation) * 0.5 * props.axis_minor_length
        y1 = y0 - math.sin(orientation) * 0.5 * props.axis_minor_length
        x2 = x0 - math.sin(orientation) * 0.5 * props.axis_major_length
        y2 = y0 - math.cos(orientation) * 0.5 * props.axis_major_length

        # ax.plot((x0, x1), (y0, y1), '-r', linewidth=2.5)
        ax.plot((x0, x2), (y0, y2), '-r', linewidth=2.5)
        ax.plot(x0, y0, '.g', markersize=15)
        # ax.text(x0 + 5, y0 + 5, f"{props.label}", fontsize='x-large',
        #         bbox={"facecolor": "red", "alpha": 0.5})

        minr, minc, maxr, maxc = props.bbox
        bx = (minc, maxc, maxc, minc, minc)
        by = (minr, minr, maxr, maxr, minr)
        # ax.plot(bx, by, '-b', linewidth=2.5)

    fig.set_dpi(200)
    ax.axis((0, labels.shape[1], labels.shape[0], 0))
    plt.show()


def hex_string_to_color(hex_string: str | list[int]):
    if not isinstance(hex_string, str):
        # assume list
        if 4 <= len(hex_string):
            return np.clip(hex_string[:4], 0, 255)
        color = np.asarray([0, 0, 0, 255])
        color[:len(hex_string)] += np.asarray(hex_string)
        return np.clip(color, 0, 255)

    if hex_string.startswith('#'):
        hex_string = hex_string[1:]

    return np.asarray([int(hex_string[:2], 16), int(hex_string[2:4], 16), int(hex_string[4:], 16), 255])


def unit_fit_for_spot(unit_mask, valid_coords, bbox_top_left, width, height):
    truth_values, counts = np.unique(
        valid_coords[bbox_top_left[1]: bbox_top_left[1] + height, bbox_top_left[0]: bbox_top_left[0] + width][unit_mask],
        return_counts=True, sorted=True)
    if len(counts) == 0:
        raise ValueError("Empty unit mask")
    elif len(counts) == 1:
        return 100 * truth_values[0]
    else:
        # [False, True]
        return counts[1] / (np.sum(counts))