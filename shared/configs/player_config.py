from dataclasses import dataclass

from pygame import surface
import pygame

from shared.constants.player_type import PlayerType


@dataclass
class PlayerConfig:
    type: PlayerType
    color: tuple
    layout: pygame.Rect
    surface: surface.Surface
