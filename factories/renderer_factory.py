from dataclasses import dataclass, field
from shared.interfaces.irenderer import IRenderer
import entity

@dataclass
class RendererFactory:
    renderers: list[IRenderer] = field(default_factory= lambda : [
        entity.court,
        entity.player_1,
        entity.player_2,
        entity.ball,
        entity.score_board
    ])

    def render(self) -> None:
        for renderer in self.renderers:
            renderer.render()