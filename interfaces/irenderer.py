from typing import Protocol

class IRenderer(Protocol):
    def render(self) -> None:
        ...