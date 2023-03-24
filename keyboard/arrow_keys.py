from dataclasses import dataclass
from typing import Sequence

import pygame


@dataclass
class ArrowKeys:
    def is_up_pressed(self, keys: Sequence[bool]) -> bool:
        return keys[pygame.K_UP]

    def is_down_pressed(self, keys: Sequence[bool]) -> bool:
        return keys[pygame.K_DOWN]
    
    def is_left_pressed(self, keys: Sequence[bool]) -> bool:
        return keys[pygame.K_LEFT]

    def is_right_pressed(self, keys: Sequence[bool]) -> bool:
        return keys[pygame.K_RIGHT]