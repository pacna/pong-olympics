from dataclasses import dataclass

from pygame import surface
import pygame

from players.types.player_type import PlayerType
from shared.types.position import Position


@dataclass
class PlayerConfig:
    type: PlayerType
    color: tuple
    layout: pygame.Rect
    surface: surface.Surface
