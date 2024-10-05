from dataclasses import dataclass, field
from shared.constants.player_type import PlayerType
from shared.types.size import Size

@dataclass
class DefaultGameConfig:
    window: Size = field(default_factory= lambda: Size(width= 1280, height= 720))
    player_name: str = "Player 1"
    player_type: PlayerType = PlayerType.SELF

    def get_window(self) -> Size:
        return self.window
    
    def get_player_name(self) -> str:
        return self.player_name
    
    def get_player_type(self) -> PlayerType:
        return self.player_type