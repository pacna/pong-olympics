from dataclasses import dataclass

from pygame import surface
import pygame

from shared.constants.player_type import PlayerType


@dataclass
class PlayerConfig:
    name: str
    type: PlayerType
    color: tuple
    layout: pygame.rect.Rect
    court_layout: pygame.rect.Rect
    surface: surface.Surface
