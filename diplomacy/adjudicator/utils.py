import copy
import itertools
import math
import re
from xml.etree.ElementTree import ElementTree, Element

import numpy as np
from lxml import etree

from diplomacy.map_parser.vector.config_player import player_data
from diplomacy.map_parser.vector.config_svg import MAP_WIDTH, RADIUS
from diplomacy.persistence.province import Location, Province, Coast


def add_arrow_definition_to_svg(svg: ElementTree) -> None:
    defs: Element = svg.find("{http://www.w3.org/2000/svg}defs")
    if defs is None:
        defs = create_element("defs", {})
        svg.getroot().append(defs)
    # TODO: Check if 'arrow' id is already defined in defs
    arrow_marker: Element = create_element(
        "marker",
        {
            "id": "arrow",
            "viewbox": "0 0 3 3",
            "refX": "1.5",
            "refY": "1.5",
            "markerWidth": "3",
            "markerHeight": "3",
            "orient": "auto-start-reverse",
        },
    )
    arrow_path: Element = create_element(
        "path",
        {"d": "M 0,0 L 3,1.5 L 0,3 z"},
    )
    arrow_marker.append(arrow_path)
    defs.append(arrow_marker)
    red_arrow_marker: Element = create_element(
        "marker",
        {
            "id": "redarrow",
            "viewbox": "0 0 3 3",
            "refX": "1.5",
            "refY": "1.5",
            "markerWidth": "3",
            "markerHeight": "3",
            "orient": "auto-start-reverse",
        },
    )
    red_arrow_path: Element = create_element(
        "path",
        {"d": "M 0,0 L 3,1.5 L 0,3 z", "fill": "red"},
    )
    red_arrow_marker.append(red_arrow_path)
    defs.append(red_arrow_marker)

    ball_marker: Element = create_element(
        "marker",
        {
            "id": "ball",
            "viewbox": "0 0 3 3",
            # "refX": "1.5",
            # "refY": "1.5",
            "markerWidth": "3",
            "markerHeight": "3",
            "orient": "auto-start-reverse",
        },
    )
    ball_def: Element = create_element(
        "circle",
        {"r": "2", "fill": "black"},
    )
    ball_marker.append(ball_def)
    defs.append(ball_marker)

    data = player_data.copy()
    data["None"] = ["ffffff"]
    for mapping in itertools.product(data, data):
        gradient_def: Element = create_element("linearGradient", {"id": f"{mapping[0]}_{mapping[1]}"})
        first: Element = create_element("stop", {"offset": "50%", "stop-color": f"#{data[mapping[0]][0]}"})
        second: Element = create_element("stop", {"offset": "50%", "stop-color": f"#{data[mapping[1]][0]}"})
        gradient_def.append(first)
        gradient_def.append(second)
        defs.append(gradient_def)


def color_element(element: Element, color: str, key="fill"):
    if len(color) == 6:  # Potentially buggy hack; just assume everything with length 6 is rgb without #
        color = f"#{color}"
    if element.get(key) is not None:
        element.set(key, color)
    if element.get("style") is not None and key in element.get("style"):
        style = element.get("style")
        style = re.sub(key + r":#[0-9a-fA-F]{6}", f"{key}:{color}", style)
        element.set("style", style)


def create_element(tag: str, attributes: dict[str, any]) -> etree.Element:
    attributes_str = {key: str(val) for key, val in attributes.items()}
    return etree.Element(tag, attributes_str)


# returns equivalent point within the map
def normalize(point: tuple[float, float] | list[float, float]) -> tuple[float, float]:
    return point[0] % MAP_WIDTH, point[1]


# returns closest point in a set
# will wrap horizontally
def sort_by_distance_to_coord(
    possibilities: set[tuple[float, float]], coord: tuple[float, float]
) -> list[list[float, float]]:
    possibilities = list(possibilities)
    possibilities_fixed = []
    crossed_map = []
    for possible_coord in possibilities:
        current_x = possible_coord[0]
        goal_x = coord[0]
        if abs(current_x - goal_x) > MAP_WIDTH / 2:
            if current_x > goal_x:
                current_x -= MAP_WIDTH
            else:
                current_x += MAP_WIDTH
            crossed_map.append(True)
        else:
            crossed_map.append(False)
        possibilities_fixed += [(current_x, possible_coord[1])]

    crossed_map = np.array(crossed_map)
    possibilities_fixed = np.array(possibilities_fixed)

    dists = np.linalg.norm(possibilities_fixed - coord, axis=1)
    # penalty for crossing map is 500 px
    sorted_indices = np.argsort(dists + 500 * crossed_map)
    return possibilities_fixed[sorted_indices].tolist()


# Note; it may return coords off the map if the closest is on the other side of the map
def get_closest_coord(possibilities: set[tuple[float, float]], coord: tuple[float, float]) -> tuple[float, float]:
    closest_coord = sort_by_distance_to_coord(possibilities, coord)[0]
    return closest_coord[0], closest_coord[1]  # Entirely just so we can return a tuple not a list


# This could be improved, but should be good enough for any sane map
# (no one is going to have like ~4 possible coords for provinces)
def match_start_to_end(
    start_points: set[tuple[float, float]], endpoints: set[tuple[float, float]]
) -> dict[tuple[float, float], tuple[float, float]]:
    endpoints = copy.copy(endpoints)
    mapping = {}
    for start in start_points:
        closest_endpoint = get_closest_coord(endpoints, start)
        mapping[start] = closest_endpoint
        endpoints.remove(normalize(closest_endpoint))
    return mapping


def loc_to_point(loc: Location, current: tuple[float, float], use_retreats=False):
    if not use_retreats:
        return get_closest_coord(loc.all_locs, current)
    else:
        return get_closest_coord(loc.all_rets, current)


def pull_coordinate(
    anchor: tuple[float, float], coordinate: tuple[float, float], pull=(1.5 * RADIUS), limit=0.25
) -> tuple[float, float]:
    """
    Pull coordinate toward anchor by a small margin to give unit view breathing room. The pull will be limited to be
    no more than the given percent of the distance because otherwise small province size areas are hard to see.
    """
    ax, ay = anchor
    cx, cy = coordinate
    dx = ax - cx
    dy = ay - cy

    distance = math.sqrt(dx**2 + dy**2)
    if distance == 0:
        return coordinate

    # if the area is small, the pull can become too large of the percent of the total arrow length
    pull = min(pull, distance * limit)

    scale = pull / distance
    return cx + dx * scale, cy + dy * scale


def order_convoys(start: Location, convoy_nodes: set[Province], end: Location) -> list[list[tuple[float, float]]]:
    layers = []
    current_layer = [start]
    next_layer = []
    for node in convoy_nodes:
        for current in current_layer:
            if isinstance(current, Province):
                if node in current.adjacent:
                    next_layer.append(node)
                    break
            elif isinstance(current, Coast):
                if node in current.adjacent_seas:
                    next_layer.append(node)
                    break
    pass
