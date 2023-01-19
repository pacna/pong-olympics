from pygame import surface, display, draw

def draw_paddle(surface: surface.Surface, x: int, y: int, width: int, height: int) -> None:
    color: tuple[int, int, int] = (255, 255, 255)
    rect: tuple[int, int, int, int] = (x, y, width, height)
    
    draw.rect(surface = surface, color = color, rect = rect)
    display.flip()
