from core.actions import *

def key_to_action(key: str):
    if key == "\x03":
        raise KeyboardInterrupt
    
    if key == "\x7f":
        return Backspace()
    
    if key == "\r":
        return Enter()
    
    if key == "\x1b":
        return None
    
    if key == "\x1a":
        return Undo()
    
    if key == "\x19":
        return Redo()
    
    if key.isprintable():
        return Insert(key)
    
    return None