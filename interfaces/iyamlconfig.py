from typing import Protocol
from shared.constants.player_type import PlayerType

from shared.types.size import Size


class IYAMLConfig(Protocol):
    def get_window(self) -> Size:
        ...
    
    def get_player_name(self) -> str:
        ...
    
    def get_player_type(self) -> PlayerType:
        ...