from pygame import surface, draw, rect, font
from shared.constants import colors, sizes
from shared.types.size import Size


def draw_paddle(surface: surface.Surface, color: tuple, layout: rect.Rect) -> None:
    draw.rect(surface = surface, color= color, rect= layout)

def draw_court(surface: surface.Surface, layout: rect.Rect) -> None:
    draw.rect(surface = surface, color= colors.WHITE, rect= layout, width = sizes.GAME_COURT_BORDER_WIDTH)

def draw_score_board(game_surface: surface.Surface, screen_size: Size, player_one_name: str, team_one_score: int, player_two_name: str, team_two_score: int) -> None:
    text: font.Font = font.Font(None, int(sizes.SCORE_FONT_SIZE)) # DON'T USE NAME ARGS. PYGAME complains about
    player_1_score: surface.Surface = text.render(str(team_one_score), False, colors.RED_DAMASK) # DON'T USE NAME ARGS. PYGAME complains about
    player_1_name: surface.Surface = text.render(player_one_name, False, colors.RED_DAMASK) # DON'T USE NAME ARGS. PYGAME complains about

    player_2_score: surface.Surface = text.render(str(team_two_score), False, colors.FRUIT_SALAD) # DON'T USE NAME ARGS. PYGAME complains about
    player_2_name: surface.Surface = text.render(str(player_two_name), False, colors.FRUIT_SALAD) # DON'T USE NAME ARGS. PYGAME complains about


    center_x: float = screen_size.width / 2
    game_surface.blit(source = player_1_score, dest = (center_x - sizes.SCORE_FONT_SIZE, sizes.SCORE_TEXT_Y_POS))
    game_surface.blit(source= player_1_name, dest=(8, sizes.SCORE_TEXT_Y_POS))

    game_surface.blit(source = player_2_score, dest = (center_x, sizes.SCORE_TEXT_Y_POS))
    # not sure why but the player 2 x pos looks a little off. Subtracting 1 to make it look even with player 1 spacing
    game_surface.blit(source = player_2_name, dest= (screen_size.width - player_2_name.get_width() - 8 - 1, sizes.SCORE_TEXT_Y_POS))

def draw_ball(surface: surface.Surface, layout: rect.Rect) -> None:
    draw.rect(surface= surface, color= colors.WHITE, rect= layout)