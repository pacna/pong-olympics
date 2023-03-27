from dataclasses import dataclass
from shared.constants.player_type import PlayerType
from shared.types.size import Size

@dataclass
class CustomYAMLConfig:
    window: Size
    player_name: str
    player_type: PlayerType

    def get_window(self) -> Size:
        return self.window
    
    def get_player_name(self) -> str:
        return self.player_name
    
    def get_player_type(self) -> PlayerType:
        return self.player_type