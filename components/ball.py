from dataclasses import dataclass

from pygame import surface, rect

from draw.draw import draw_ball


@dataclass
class Ball:
    surface: surface.Surface
    court_layout: rect.Rect

    def render(self) -> None:
        draw_ball(surface= self.surface, court_layout= self.court_layout)