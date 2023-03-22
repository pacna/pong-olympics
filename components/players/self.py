from dataclasses import dataclass
from typing import Sequence

import pygame
from draw import draw_paddle

from shared.constants.player_type import PlayerType
from shared.types.position import Position
from shared.constants import speed, sizes

@dataclass
class Self:
    color: tuple
    surface: pygame.surface.Surface
    layout: pygame.rect.Rect
    court_layout: pygame.rect.Rect
    type: PlayerType = PlayerType.SELF

    def get_type(self) -> PlayerType:
        return self.type

    def get_layout(self) -> pygame.rect.Rect:
        return self.layout

    def render(self) -> None:
        draw_paddle(surface=self.surface, color=self.color, layout= self.layout)

    def update(self, keys: Sequence[bool]) -> None:
        if self._is_up_pressed(keys = keys):
            self._update_pos(pos = Position(x = 0, y = -speed.PADDLE_SPEED))
        if self._is_down_pressed(keys = keys):
            self._update_pos(pos = Position(x = 0, y = speed.PADDLE_SPEED))  
    
    def _update_pos(self, pos: Position) -> None:
        updated_layout: pygame.rect.Rect = self.layout.move(pos.x, pos.y)
        player_upper_paddle: float = updated_layout.y
        player_bottom_paddle: float = updated_layout.y + updated_layout.height
        court_upper_wall: float = self.court_layout.y + sizes.GAME_COURT_BORDER_WIDTH
        court_bottom_wall: float = self.court_layout.height + self.court_layout.y - sizes.GAME_COURT_BORDER_WIDTH

        # check if the player is within the court
        if player_upper_paddle < court_upper_wall or player_bottom_paddle > court_bottom_wall:
            return

        self.layout = updated_layout

    def _is_up_pressed(self, keys: Sequence[bool]) -> bool:
        return keys[pygame.K_w]
    
    def _is_down_pressed(self, keys: Sequence[bool]) -> bool:
        return keys[pygame.K_s]
    
