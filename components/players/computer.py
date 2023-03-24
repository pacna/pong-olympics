from dataclasses import dataclass, field
from typing import Sequence
from keyboard.empty_keys import EmptyKeys
from interfaces.ikeyboard import IKeyBoard
from shared.constants.player_type import PlayerType
from shared.types.position import Position
from shared.constants import speed, sizes
from .base_player import BasePlayer

@dataclass
class Computer(BasePlayer):
    type: PlayerType = PlayerType.COMPUTER
    input: IKeyBoard = field(default_factory= EmptyKeys)

    def get_type(self) -> PlayerType:
        return self.type

    def update(self, keys: Sequence[bool]) -> None:
        if self.input.is_up_pressed(keys = keys):
            self._update_pos(pos = Position(x = 0, y = -speed.PADDLE_SPEED))
        if self.input.is_down_pressed(keys = keys):
            self._update_pos(pos = Position(x = 0, y = speed.PADDLE_SPEED))
    
    def _update_pos(self, pos: Position) -> None:
        court_upper_wall: float = self.court_layout.y + sizes.GAME_COURT_BORDER_WIDTH
        court_bottom_wall: float = self.court_layout.height + self.court_layout.y - sizes.GAME_COURT_BORDER_WIDTH

        # layout uses standard coordinates so (0,0) starts at the center
        self.layout = self.layout.move(pos.x, pos.y)
        self.layout.top = max(court_upper_wall, self.layout.top)
        self.layout.bottom = min(court_bottom_wall, self.layout.bottom)