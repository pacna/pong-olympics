from uuid import uuid4
from components.paddle import draw_paddle

from players.types.player_config import PlayerConfig
from shared.types.size import Size


class Player:
    def __init__(self, config: PlayerConfig) -> None:
        self.id = str(uuid4())
        self.config = config

    def render(self) -> None:
        draw_paddle(surface=self.config.surface, color=self.config.color, position=self.config.position, size=Size(width= 10, height= 40))