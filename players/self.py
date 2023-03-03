from dataclasses import dataclass

import pygame
from draw.draw import draw_paddle

from players.types.player_type import PlayerType
from shared.types.position import Position

@dataclass
class Self:
    color: tuple
    surface: pygame.surface.Surface
    layout: pygame.rect.Rect
    type: PlayerType = PlayerType.SELF

    def get_type(self) -> PlayerType:
        return self.type

    def render(self) -> None:
        draw_paddle(surface=self.surface, color=self.color, layout= self.layout)

    def update(self, key: int) -> None:
        if self._is_up_pressed(key):
            self._update_pos(pos = Position(x = 0, y = -1))
        if self._is_down_pressed(key):
            self._update_pos(pos = Position(x = 0, y = 1))
    
    def _update_pos(self, pos: Position) -> None:
        self.layout = self.layout.move(pos.x, pos.y)

    def _is_up_pressed(self, key: int) -> bool:
        return key == pygame.K_w
    
    def _is_down_pressed(self, key: int) -> bool:
        return key == pygame.K_s
    
