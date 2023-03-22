from dataclasses import dataclass

from pygame import surface

from draw import draw_score_board
from shared.types.size import Size


@dataclass
class ScoreBoard:
    surface: surface.Surface
    screen_size: Size

    def render(self) -> None:
        draw_score_board(game_surface= self.surface, screen_size= self.screen_size)