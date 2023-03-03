from pygame import surface, display, draw, Rect
from shared.constants import colors, sizes


def draw_paddle(surface: surface.Surface, color: tuple, layout: Rect) -> None:
    draw.rect(surface = surface, color= color, rect= layout)
    display.flip()


def draw_court(surface: surface.Surface, layout: Rect) -> None:
    draw.rect(surface = surface, color= colors.WHITE, rect= layout, width = sizes.GAME_COURT_BORDER_WIDTH)
    display.flip()