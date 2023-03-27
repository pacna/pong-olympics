from pygame import surface, rect
from dataclasses import dataclass
from shared.draw import draw_paddle

@dataclass
class BasePlayer():
    name: str
    color: tuple
    surface: surface.Surface
    layout: rect.Rect
    court_layout: rect.Rect

    def get_layout(self) -> rect.Rect:
        return self.layout
    
    def get_name(self) -> str:
        return self.name

    def render(self) -> None:
        draw_paddle(surface=self.surface, color=self.color, layout= self.layout)