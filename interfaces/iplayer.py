from typing import Protocol, Sequence

import pygame

from shared.constants.player_type import PlayerType


class IPlayer(Protocol):
    def get_type(self) -> PlayerType:
        ...
    def get_layout(self) -> pygame.rect.Rect:
        ...
    def render(self) -> None:
        ...
    def update(self, keys: Sequence[bool]) -> None:
        ...