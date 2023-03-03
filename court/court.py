from pygame import rect, surface
from dataclasses import dataclass
from draw.draw import draw_court


@dataclass
class Court:
    surface: surface.Surface
    layout: rect.Rect

    def render(self) -> None:
        draw_court(surface= self.surface, layout = self.layout)