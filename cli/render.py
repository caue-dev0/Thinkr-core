import os
import sys
from core.state import EditorState

def render(state: EditorState):
    os.system("clear")

    for i, line in enumerate(state.lines):
        if i == state.line:
            before = line[:state.col]
            after = line[state.col:]
            print(before + "|" + after)
        else:
            print(line)

    sys.stdout.flush()