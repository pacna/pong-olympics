from typing import Protocol

from players.types.player_type import PlayerType


class IPlayer(Protocol):
    def get_type(self) -> PlayerType:
        ...
    def render(self) -> None:
        ...
    def update(self, key: int) -> None:
        ...