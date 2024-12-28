from diplomacy.adjudicator.mapper import Mapper
from diplomacy.map_parser.vector.vector import Parser
from diplomacy.persistence.order import Move, Support
from diplomacy.adjudicator.adjudicator import MovesAdjudicator


def run():
    parser = Parser()
    board = parser.parse()

    novgorod = board.get_province("Novgorod")
    moscow = board.get_province("Moscow")
    kyiv = board.get_province("Kyiv")
    kursk = board.get_province("Kursk")

    novgorod.unit.order = Move(kursk)
    moscow.unit.order = Support(novgorod.unit, kursk)
    kyiv.unit.order = Move(kursk)

    mapper = Mapper(board)

    adjudicator = MovesAdjudicator(board)
    adjudicator.run()

    mapper.draw_moves_map(board.phase, None)
