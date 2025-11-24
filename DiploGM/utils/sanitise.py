
import re


def sanitise_name(str):
    str = re.sub(r"[‘’`´′‛.']", "", str)
    str = re.sub(r"-", " ", str)
    return str


# I'm sorry this is a bad function name. I couldn't think of anything better and I'm in a rush
def simple_player_name(name: str):
    return name.lower().replace("-", " ").replace("'", "").replace(".", "")
