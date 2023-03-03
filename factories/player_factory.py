from components.players.computer import Computer
from shared.interfaces.iplayer import IPlayer
from components.players.opponent import Opponent
from components.players.self import Self
from shared.configs.player_config import PlayerConfig
from shared.constants.player_type import PlayerType


def create_player_factory(config: PlayerConfig) -> IPlayer:
    match config.type:
        case PlayerType.SELF:
            return Self(surface= config.surface, color= config.color, layout= config.layout)
        case PlayerType.OPPONENT:
            return Opponent(surface= config.surface, color= config.color, layout= config.layout)
        case PlayerType.COMPUTER:
            return Computer(surface= config.surface, color= config.color, layout= config.layout)
        case _:
            return Computer(surface= config.surface, color= config.color, layout= config.layout)

