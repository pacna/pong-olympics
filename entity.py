from components.ball import Ball
from components.court import Court
from factories.message_bus.message_bus_factory import MessageBusFactory
from interfaces.iplayer import IPlayer
from components.score_board import ScoreBoard


player_1: IPlayer
player_2: IPlayer

court: Court
score_board: ScoreBoard
ball: Ball

msg_bus: MessageBusFactory
