from pygame import surface, draw, rect, font
from shared.constants import colors, sizes
from shared.types.size import Size


def draw_paddle(surface: surface.Surface, color: tuple, layout: rect.Rect) -> None:
    draw.rect(surface = surface, color= color, rect= layout)

def draw_court(surface: surface.Surface, layout: rect.Rect) -> None:
    draw.rect(surface = surface, color= colors.WHITE, rect= layout, width = sizes.GAME_COURT_BORDER_WIDTH)

def draw_score_board(game_surface: surface.Surface, screen_size: Size, team_one_score: int, team_two_score: int) -> None:
    text: font.Font = font.Font(None, int(sizes.SCORE_FINAL_SIZE)) # DON'T USE NAME ARGS. PYGAME complains about
    player_1_score_text: surface.Surface = text.render(str(team_one_score), False, colors.RED_DAMASK) # DON'T USE NAME ARGS. PYGAME complains about

    player_2_score_text: surface.Surface = text.render(str(team_two_score), False, colors.FRUIT_SALAD) # DON'T USE NAME ARGS. PYGAME complains about
    center_x: float = screen_size.width / 2
    game_surface.blit(source = player_1_score_text, dest = (center_x - sizes.SCORE_FINAL_SIZE, 40))
    game_surface.blit(source = player_2_score_text, dest = (center_x + sizes.SCORE_FINAL_SIZE, 40))

def draw_ball(surface: surface.Surface, layout: rect.Rect) -> None:
    draw.circle(surface= surface, color= colors.WHITE, center= (layout.centerx, layout.centery), radius = sizes.BALL_RADIUS)