from dataclasses import dataclass;

class Action:
    pass

@dataclass(frozen=True)
class Insert(Action):
    value: str

class Backspace():
    pass

class Enter(Action):
    pass


class MoveLeft(Action):
    pass

class MoveRight(Action):
    pass

class MoveUp(Action):
    pass

class MoveDown(Action):
    pass