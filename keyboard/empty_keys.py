from dataclasses import dataclass
from typing import Sequence

@dataclass
class EmptyKeys:
    def is_up_pressed(self, keys: Sequence[bool]) -> bool:
        return True

    def is_down_pressed(self, keys: Sequence[bool]) -> bool:
        return True
    
    def is_left_pressed(self, keys: Sequence[bool]) -> bool:
        return True

    def is_right_pressed(self, keys: Sequence[bool]) -> bool:
        return True
