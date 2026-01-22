import sys
import tty
import termios

from core.state import create_state
from core.history import create_history
from core.dispatch_history import dispatch_history
from cli.keymap import key_to_action
from cli.render import render

def read_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

    return ch

def main():
    history = create_history(create_state())

    while True:
        render(history.present)

        key = read_key()
        action = key_to_action(key)

        if action:
            history = dispatch_history(history, action)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaindo...")