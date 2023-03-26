from dataclasses import dataclass, field
from typing import Sequence
from interfaces.irenderer import IRenderer
import entity

@dataclass
class RendererFactory:
    renderers: Sequence[IRenderer] = field(default_factory= lambda : [
        entity.court,
        entity.player_1,
        entity.player_2,
        entity.ball,
        entity.score_board
    ])

    def render(self) -> None:
        for renderer in self.renderers:
            renderer.render()