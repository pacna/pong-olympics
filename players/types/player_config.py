from dataclasses import dataclass

from pygame import surface

from players.types.player_type import PlayerType
from shared.types.position import Position


@dataclass
class PlayerConfig:
    type: PlayerType
    color: tuple
    position: Position
    surface: surface.Surface
