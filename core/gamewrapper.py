import pygame

from components.paddle import draw_paddle

def run_program() -> None:
    pygame.init()
    pygame.display.set_caption('Pygame Pong')

    surface: pygame.surface.Surface = pygame.display.set_mode(size = (1280, 720))

    __init(surface = surface)

    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit() # to properly quit out of the program

def __init(surface: pygame.surface.Surface) -> None:
    draw_paddle(surface=surface, x = 0, y = 0, width= 10, height = 40)
    draw_paddle(surface=surface, x = 1270, y = 0, width= 10, height = 40)
