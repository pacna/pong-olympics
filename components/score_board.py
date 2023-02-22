
from pygame import surface
from shared.constants import colors
import pygame


def draw_score_board(game_surface: surface.Surface) -> None:
    text: pygame.font.Font = pygame.font.Font(None, 100) # DON'T USE NAME ARGS. PYGAME complains about
    player_1_score_text: surface.Surface = text.render('1', False, colors.RED_DAMASK) # DON'T USE NAME ARGS. PYGAME complains about

    # text: pygame.font.Font = pygame.font.Font(None, 40) # DON'T USE NAME ARGS. PYGAME complains about
    player_2_score_text: surface.Surface = text.render('2', False, colors.FRUIT_SALAD) # DON'T USE NAME ARGS. PYGAME complains about
    game_surface.blit(source = player_1_score_text, dest = (600, 40))
    game_surface.blit(source = player_2_score_text, dest = (1280 - 600, 40))