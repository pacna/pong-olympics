from dataclasses import dataclass, field
from typing import Sequence
from shared.interfaces.irenderer import IRenderer
import core.entity as entity

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