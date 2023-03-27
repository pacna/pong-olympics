from dataclasses import dataclass, field
from components.players.base_player import BasePlayer
from shared.interfaces.ikeyboard import IKeyBoard
from shared.constants.player_type import PlayerType
from shared.keyboard.empty_keys import EmptyKeys

@dataclass
class MockPlayer(BasePlayer):
    type: PlayerType = PlayerType.SELF
    input: IKeyBoard = field(default_factory= EmptyKeys)

    def get_type(self) -> PlayerType:
        return self.type
    
    def update(self) -> None:
        ...
