from dataclasses import dataclass
from pygame import surface, rect
from draw import draw_ball
from shared.constants import speed

@dataclass
class Ball:
    surface: surface.Surface
    layout: rect.Rect

    def render(self) -> None:
        draw_ball(surface= self.surface, layout= self.layout)

    def update(self) -> None:
        self.layout = self.layout.move(-speed.BALL_SPEED, 0)