from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from diplomacy.persistence.player import Player
    from diplomacy.persistence.province import Province, Coast


class UnitType(Enum):
    ARMY = 1
    FLEET = 2


class Unit:
    def __init__(
        self,
        coordinate: tuple[float, float],
        radius: float,
        unit_type: UnitType,
        player: Player,
        province: Province,
    ):
        self.coordinate: tuple[float, float] = coordinate
        self.radius: float = radius

        self.unit_type: UnitType = unit_type
        self.player: Player = player
        self.province: Province = province

        self.coast: Coast | None = None
        "retreat_options is None when not dislodged and {} when dislodged without retreat options"
        self.retreat_options: set[Province] | None = None

    def __str__(self):
        return f"{self.unit_type.__class__} {self.player} {self.province}"
