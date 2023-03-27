from dataclasses import dataclass, field
from typing import Sequence
from shared.keyboard.empty_keys import EmptyKeys
from shared.interfaces.ikeyboard import IKeyBoard
from shared.constants.player_type import PlayerType
from shared.types.position import Position
from shared.constants import speed, sizes
from .base_player import BasePlayer
import random

@dataclass
class Computer(BasePlayer):
    type: PlayerType = PlayerType.COMPUTER
    input: IKeyBoard = field(default_factory= EmptyKeys)
    should_go_up: bool = field(default_factory= lambda : True if 0 > random.randint(-1, 2) else False) 

    def get_type(self) -> PlayerType:
        return self.type

    def update(self, keys: Sequence[bool]) -> None:
        court_upper_wall: float = self.court_layout.y + sizes.GAME_COURT_BORDER_WIDTH
        court_bottom_wall: float = self.court_layout.height + self.court_layout.y - sizes.GAME_COURT_BORDER_WIDTH

        if self.layout.top <= court_upper_wall:
            self.should_go_up = False
        if self.layout.bottom >= court_bottom_wall:
            self.should_go_up = True

        if self.input.is_up_pressed(keys = keys) and self.should_go_up:
            self._update_pos(pos = Position(x = 0, y = -speed.PADDLE_SPEED))
        if self.input.is_down_pressed(keys = keys) and not self.should_go_up:
            self._update_pos(pos = Position(x = 0, y = speed.PADDLE_SPEED))
    
    def _update_pos(self, pos: Position) -> None:
        court_upper_wall: float = self.court_layout.y + sizes.GAME_COURT_BORDER_WIDTH
        court_bottom_wall: float = self.court_layout.height + self.court_layout.y - sizes.GAME_COURT_BORDER_WIDTH

        self.layout = self.layout.move(pos.x, pos.y)
        self.layout.top = max(court_upper_wall, self.layout.top)
        self.layout.bottom = min(court_bottom_wall, self.layout.bottom)