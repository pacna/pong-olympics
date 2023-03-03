from pygame import Rect, surface
from components.ball import Ball
from components.court import Court
from factories.player_factory import create_player_factory
from shared.configs.player_config import PlayerConfig
from shared.constants.player_type import PlayerType
from components.score_board import ScoreBoard
from shared.types.position import Position
from shared.types.size import Size
from shared.constants import sizes, colors
from pieces import pieces

def load_world(surface: surface.Surface, screen_size: Size) -> None:
    _load_court(surface= surface, screen_size= screen_size)
    _load_score_board(surface= surface, screen_size= screen_size)
    _load_player(surface= surface, screen_size= screen_size)
    _load_ball(surface= surface)

def _load_court(surface: surface.Surface, screen_size: Size) -> None:
    pieces.court = Court(surface=surface, layout= Rect(0, sizes.GAME_COURT_HEIGHT, screen_size.width, screen_size.height - sizes.GAME_COURT_HEIGHT))

def _load_score_board(surface: surface.Surface, screen_size: Size) -> None:
    pieces.score_board = ScoreBoard(surface= surface, screen_size= screen_size)

def _load_player(surface: surface.Surface, screen_size: Size) -> None:
    player_1_pos = Position(x = pieces.court.layout.x + sizes.GAME_COURT_BORDER_WIDTH, y = pieces.court.layout.centery - ((sizes.PLAYER_WIDTH + sizes.GAME_COURT_BORDER_WIDTH) * 2))
    player_2_pos = Position(x = screen_size.width - (sizes.PLAYER_WIDTH + sizes.GAME_COURT_BORDER_WIDTH), y = pieces.court.layout.centery - ((sizes.PLAYER_WIDTH + sizes.GAME_COURT_BORDER_WIDTH) * 2))

    pieces.player_1 = create_player_factory(config= PlayerConfig(
        surface= surface, 
        color=colors.RED_DAMASK,
        layout= Rect(player_1_pos.x, player_1_pos.y, sizes.PLAYER_WIDTH, sizes.PLAYER_HEIGHT), 
        type= PlayerType.SELF))

    pieces.player_2 = create_player_factory(config= PlayerConfig(
        surface= surface, 
        color=colors.FRUIT_SALAD,
        layout=Rect(player_2_pos.x, player_2_pos.y, sizes.PLAYER_WIDTH, sizes.PLAYER_HEIGHT),
        type= PlayerType.OPPONENT))
    
def _load_ball(surface: surface.Surface) -> None:
    pieces.ball = Ball(surface= surface, court_layout= pieces.court.layout)