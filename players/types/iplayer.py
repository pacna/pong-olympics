from typing import Protocol


class IPlayer(Protocol):
    id: str
    def render(self) -> None:
        ...