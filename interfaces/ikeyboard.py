from typing import Protocol, Sequence

class IKeyBoard(Protocol):
    def is_up_pressed(self, keys: Sequence[bool]) -> bool:
        ...

    def is_down_pressed(self, keys: Sequence[bool]) -> bool:
        ...

    def is_left_pressed(self, keys: Sequence[bool]) -> bool:
        ...

    def is_right_pressed(self, keys: Sequence[bool]) -> bool:
        ...