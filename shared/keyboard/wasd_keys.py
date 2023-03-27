from dataclasses import dataclass
from typing import Sequence
import pygame


@dataclass
class WASDKeys:
    def is_up_pressed(self, keys: Sequence[bool]) -> bool:
        return keys[pygame.K_w]

    def is_down_pressed(self, keys: Sequence[bool]) -> bool:
        return keys[pygame.K_s]
    
    def is_left_pressed(self, keys: Sequence[bool]) -> bool:
        return keys[pygame.K_a]

    def is_right_pressed(self, keys: Sequence[bool]) -> bool:
        return keys[pygame.K_d]