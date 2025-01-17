import logging

from diplomacy.adjudicator.mapper import Mapper
from diplomacy.map_parser.vector.vector import Parser
from diplomacy.persistence.order import Move, Support, Hold, RetreatMove
from diplomacy.adjudicator.adjudicator import MovesAdjudicator, RetreatsAdjudicator
from diplomacy.persistence.unit import Unit, UnitType


def run():
    parser = Parser()
    board = parser.parse()

    for unit in board.units:
        unit.order = Hold()

    novgorod = board.get_province("Novgorod")
    moscow = board.get_province("Moscow")
    kyiv = board.get_province("Kyiv")
    kursk = board.get_province("Kursk")
    helsingfors = board.get_province("Helsingfors")
    baltic_sea = board.get_province("Baltic Sea")

    russia = board.get_player("Russia")

    # novgorod.unit.order = Move(kursk)
    # moscow.unit.order = Support(novgorod.unit, kursk)
    # kyiv.unit.order = Move(kursk)
    # helsingfors.get_unit().order = Move(baltic_sea)

    kyiv.dislodged_unit = Unit(UnitType.ARMY, russia, kyiv, None, {kursk})
    russia.units.add(kyiv.dislodged_unit)
    board.units.add(kyiv.dislodged_unit)
    kyiv.dislodged_unit.order = RetreatMove(kursk)

    mapper = Mapper(board)

    # adjudicator = MovesAdjudicator(board)
    adjudicator = RetreatsAdjudicator(board)
    adjudicator.run()

    mapper.draw_moves_map(adjudicator, None)
