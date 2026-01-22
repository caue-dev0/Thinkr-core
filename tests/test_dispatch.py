from core.state import create_state
from core.dispatch import dispatch
from core.actions import *

def test_insert_and_move():
    state = create_state()
    state = dispatch(state, Insert("h"))
    state = dispatch(state, Insert("i"))
    state = dispatch(state, MoveLeft())
    state = dispatch(state, Insert("!"))

    assert state.lines == ["h!i"]
    assert state.line == 0
    assert state.col == 2
