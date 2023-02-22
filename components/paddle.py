from pygame import surface, display, draw, Rect
from shared.types import size, position


def draw_paddle(surface: surface.Surface, color: tuple, position: position.Position, size: size.Size) -> None:
    paddle_size: Rect = Rect(position.x, position.y, size.width, size.height)
    draw.rect(surface = surface, color= color, rect= paddle_size)
    display.flip()
