from components.ball import Ball
from components.court import Court
from factories.message_bus.bus import Bus
from factories.message_bus.publisher import Publisher
from shared.interfaces.iplayer import IPlayer
from components.score_board import ScoreBoard


player_1: IPlayer
player_2: IPlayer

court: Court
score_board: ScoreBoard
ball: Ball

publisher: Publisher
message_bus: Bus
