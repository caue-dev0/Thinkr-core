from core.state import EditorState

def insert_text(state: EditorState, value: str) -> EditorState:
    lines = state.lines
    line = state.line
    col = state.col

    current_line =  lines[line]
    before = current_line[:col]
    after = current_line[col:]

    new_line = before + value + after

    new_lines = lines.copy()
    new_lines[line] = new_line

    return EditorState(
        lines=new_lines,
        line=line,
        col=col + len(value)
    )

def backspace(state: EditorState) -> EditorState:
    lines = state.lines
    line = state.line
    col = state.col

    if line == 0 and col == 0:
        return state
    
    if col > 0:
        current_line = lines[line]
        before = current_line[:col - 1]
        after = current_line[col:]

        new_line = before + after

        new_lines = lines.copy()
        new_lines[line] = new_line

        return EditorState(
            lines=new_lines,
            line=new_line,
            col=col -1
        )
    
    prev_line = lines[line - 1]
    current_line = lines[line]

    merged_line = prev_line + current_line

    new_lines = lines.copy()
    new_lines[line - 1] = merged_line
    new_lines.pop(line)

    return EditorState(
        lines=new_lines,
        line=new_line,
        col=len(prev_line)
    )