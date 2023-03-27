from typing import Callable
from pygame import surface, rect
from components.ball import Ball
from components.court import Court
from factories.message_bus.message_bus_factory import MessageBusFactory
from factories.player_factory import create_player_factory
from interfaces.iyamlconfig import IYAMLConfig
from shared.configs.player_config import PlayerConfig
from shared.constants.player_type import PlayerType
from components.score_board import ScoreBoard
from shared.types.position import Position
from shared.types.size import Size
from shared.constants import sizes, colors, speed
from config import config_yaml
import random
import entity

def load_world(surface: surface.Surface, screen_size: Size, config: IYAMLConfig) -> None:
    _load_court(surface= surface, screen_size= screen_size)
    _load_player(surface= surface, screen_size= screen_size, config= config)
    _load_score_board(surface= surface, screen_size= screen_size)
    _load_ball(surface= surface)
    _load_msg_bus()

def _load_court(surface: surface.Surface, screen_size: Size) -> None:
    entity.court = Court(surface=surface, layout= rect.Rect(0, sizes.GAME_COURT_HEIGHT, screen_size.width, screen_size.height - sizes.GAME_COURT_HEIGHT))

def _load_score_board(surface: surface.Surface, screen_size: Size) -> None:
    entity.score_board = ScoreBoard(surface= surface, screen_size= screen_size, player_1_name=entity.player_1.get_name(), player_2_name= entity.player_2.get_name())

def _load_player(surface: surface.Surface, screen_size: Size, config: IYAMLConfig) -> None:
    player_1_pos = Position(x = entity.court.layout.x + sizes.GAME_COURT_BORDER_WIDTH, y = entity.court.layout.centery - ((sizes.PLAYER_WIDTH + sizes.GAME_COURT_BORDER_WIDTH) * 2))
    player_2_pos = Position(x = screen_size.width - (sizes.PLAYER_WIDTH + sizes.GAME_COURT_BORDER_WIDTH), y = entity.court.layout.centery - ((sizes.PLAYER_WIDTH + sizes.GAME_COURT_BORDER_WIDTH) * 2))

    player_config_type: PlayerType = config.get_player_type()

    entity.player_1 = create_player_factory(
        config=PlayerConfig(
            name="Player 1" if player_config_type != PlayerType.OPPONENT else config_yaml.get_player_name(),
            surface=surface,
            color=colors.RED_DAMASK,
            layout=rect.Rect(player_1_pos.x, player_1_pos.y, sizes.PLAYER_WIDTH, sizes.PLAYER_HEIGHT),
            type=PlayerType.SELF if player_config_type == PlayerType.SELF else PlayerType.COMPUTER,
            court_layout=entity.court.layout
        )
    )

    entity.player_2 = create_player_factory(
        config=PlayerConfig(
            name="Player 2" if player_config_type != PlayerType.SELF else config_yaml.get_player_name(),
            surface=surface,
            color=colors.FRUIT_SALAD,
            layout=rect.Rect(player_2_pos.x, player_2_pos.y, sizes.PLAYER_WIDTH, sizes.PLAYER_HEIGHT),
            type=PlayerType.OPPONENT if player_config_type == PlayerType.OPPONENT else PlayerType.COMPUTER,
            court_layout=entity.court.layout
        )
    )
    
def _load_ball(surface: surface.Surface) -> None:
    create_circle_point: Callable[[int], float] = lambda xy: xy - (sizes.GAME_COURT_BORDER_WIDTH * 2)
    create_direction: Callable[[int], float] = lambda rand: speed.BALL_SPEED if rand > 0 else -speed.BALL_SPEED
 
    ball_pos: Position = Position(x = create_circle_point(entity.court.layout.centerx), y = entity.court.layout.centery - create_circle_point(sizes.GAME_COURT_BORDER_WIDTH * 2))

    entity.ball = Ball(
        surface= surface, 
        layout= rect.Rect(
            ball_pos.x,
            ball_pos.y,
            sizes.BALL_HEIGHT_WIDTH,
            sizes.BALL_HEIGHT_WIDTH
        ),
        x_velocity= create_direction(random.randint(-1, 2)),
        y_velocity= create_direction(random.randint(-1, 2)),
        court_layout= entity.court.layout)
    
def _load_msg_bus() -> None:
    entity.msg_bus = MessageBusFactory()