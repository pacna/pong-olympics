from pygame import Rect, surface, display
from dataclasses import dataclass
from components.paddle import draw_court


@dataclass
class Court:
    surface: surface.Surface
    layout: Rect

    def render(self) -> None:
        draw_court(surface= self.surface, layout = self.layout)
        display.flip()