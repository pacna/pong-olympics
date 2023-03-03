from pygame import surface, draw, rect, font
from shared.constants import colors, sizes
from shared.types.size import Size


def draw_paddle(surface: surface.Surface, color: tuple, layout: rect.Rect) -> None:
    draw.rect(surface = surface, color= color, rect= layout)


def draw_court(surface: surface.Surface, layout: rect.Rect) -> None:
    draw.rect(surface = surface, color= colors.WHITE, rect= layout, width = sizes.GAME_COURT_BORDER_WIDTH)

def draw_score_board(game_surface: surface.Surface, screen_size: Size) -> None:
    text: font.Font = font.Font(None, int(sizes.SCORE_FINAL_SIZE)) # DON'T USE NAME ARGS. PYGAME complains about
    player_1_score_text: surface.Surface = text.render('0', False, colors.RED_DAMASK) # DON'T USE NAME ARGS. PYGAME complains about

    player_2_score_text: surface.Surface = text.render('0', False, colors.FRUIT_SALAD) # DON'T USE NAME ARGS. PYGAME complains about
    center_x: float = screen_size.width / 2
    game_surface.blit(source = player_1_score_text, dest = (center_x - sizes.SCORE_FINAL_SIZE, 40))
    game_surface.blit(source = player_2_score_text, dest = (center_x + sizes.SCORE_FINAL_SIZE, 40))

def draw_ball(surface: surface.Surface, court_layout: rect.Rect) -> None:
    draw.circle(surface= surface, color= colors.WHITE, center= (court_layout.centerx - sizes.BALL_RADIUS, court_layout.centery - sizes.BALL_RADIUS), radius = sizes.BALL_RADIUS)