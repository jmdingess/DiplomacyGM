from diplomacy.adjudicator.adjudicator import MovesAdjudicator
from diplomacy.adjudicator.mapper import Mapper
from diplomacy.map_parser.vector.vector import Parser
from diplomacy.persistence.order import Move, Support, Hold, ConvoyTransport
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
    umea = board.get_province("Umea")
    baltic_sea = board.get_province("Baltic Sea")
    gulf_of_bothnia = board.get_province("Gulf of Bothnia")
    brandenburg = board.get_province("Brandenburg")
    warsaw = board.get_province("Warsaw")

    russia = board.get_player("Russia")

    novgorod.unit.order = Move(kursk)
    moscow.unit.order = Support(novgorod.unit, kursk)
    kyiv.unit.order = Move(kursk)
    helsingfors.get_unit().order = Move(baltic_sea)
    warsaw.unit.order = None

    gulf_of_bothnia.unit = Unit(UnitType.FLEET, russia, gulf_of_bothnia, None, None)
    baltic_sea.unit = Unit(UnitType.FLEET, russia, baltic_sea, None, None)
    board.units.add(gulf_of_bothnia.unit)
    board.units.add(baltic_sea.unit)
    russia.units.add(gulf_of_bothnia.unit)
    russia.units.add(baltic_sea.unit)

    gulf_of_bothnia.unit.order = ConvoyTransport(umea.unit, brandenburg)
    baltic_sea.unit.order = ConvoyTransport(umea.unit, brandenburg)
    umea.unit.order = Move(brandenburg)

    # kyiv.dislodged_unit = Unit(UnitType.ARMY, russia, kyiv, None, {kursk})
    # russia.units.add(kyiv.dislodged_unit)
    # board.units.add(kyiv.dislodged_unit)
    # kyiv.dislodged_unit.order = RetreatMove(kursk)

    mapper = Mapper(board)

    # adjudicator = RetreatsAdjudicator(board)
    adjudicator = MovesAdjudicator(board)
    adjudicator.run()

    mapper.draw_moves_map(adjudicator, None)
