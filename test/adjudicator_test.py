from diplomacy.pydip_adjudicator.adjudicator import Adjudicator
from diplomacy.map_parser.vector import vector
from diplomacy.persistence import order
from diplomacy.persistence.board import Board
from diplomacy.persistence.unit import UnitType


# the pydip library is not super clear, so we're going to have some tests around here that let us figure out what's
# going on via the debugger.
def run() -> None:
    board = vector.Parser().parse()

    # spring moves
    paris = board.get_province("Paris")
    ghent = board.get_province("Ghent")
    paris.unit.order = order.Move(ghent)
    _adjudicate(board)

    # spring retreats
    _adjudicate(board)

    # fall moves
    amsterdam = board.get_province("Amsterdam")
    utrecht = board.get_province("Utrecht")
    amsterdam.unit.order = order.Move(ghent.coast())
    utrecht.unit.order = order.Support(amsterdam.unit, ghent.coast())
    _adjudicate(board)

    # fall retreats
    ghent.dislodged_unit.order = order.RetreatMove(paris)
    _adjudicate(board)

    # builds
    netherlands = board.get_player("Netherlands")
    netherlands.build_orders.add(order.Build(amsterdam.coast(), UnitType.FLEET))
    _adjudicate(board)


def _adjudicate(board: Board) -> None:
    adjudicator = Adjudicator(board)
    adjudicator.adjudicate()
