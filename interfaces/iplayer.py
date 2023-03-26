from typing import Protocol, Sequence
from shared.constants.player_type import PlayerType
import pygame


class IPlayer(Protocol):
    def get_type(self) -> PlayerType:
        ...
    def get_name(self) -> str:
        ...
    def get_layout(self) -> pygame.rect.Rect:
        ...
    def render(self) -> None:
        ...
    def update(self, keys: Sequence[bool]) -> None:
        ...