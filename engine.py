from typing import Sequence
from collision_facade import CollisionFacade
from factories.renderer_factory import RendererFactory
from shared.configs.game_config import GameConfig
from shared.constants import colors
from shared.constants.player_type import PlayerType
from shared.types.size import Size
from world import load_world
import pygame
import entity

class Engine:
    def __init__(self, config: GameConfig) -> None:
        self.config = config
        self.surface = pygame.display.set_mode(size = (self.config.width, self.config.height))

    def run(self) -> None:
        self._load()
        self._run_game()

    def _load(self) -> None:
        pygame.display.set_caption(self.config.title)
        load_world(surface= self.surface, screen_size= Size(width= self.config.width, height= self.config.height))

    def _update(self) -> None:
        entity.ball.update()
        CollisionFacade().collide()
        entity.msg_bus.run()

    def _keypressed(self, keys: Sequence[bool], is_keydown_hold: bool) -> None:
        player1_type = entity.player_1.get_type()
        player2_type = entity.player_2.get_type()

        if is_keydown_hold:
            if player1_type is not PlayerType.COMPUTER:
                entity.player_1.update(keys=keys)
            if player2_type is not PlayerType.COMPUTER:
                entity.player_2.update(keys=keys)

        if player1_type is PlayerType.COMPUTER:
            entity.player_1.update(keys=keys)
        if player2_type is PlayerType.COMPUTER:
            entity.player_2.update(keys=keys)


    def _draw(self) -> None:
        RendererFactory().render()

    def _exit(self) -> None:
        pygame.quit()
        quit() # to properly quit out of the program

    def _run_game(self) -> None:
        clock: pygame.time.Clock = pygame.time.Clock()
        is_key_hold: bool = False
        while True:
            for event in pygame.event.get():
               match event.type:
                    case pygame.QUIT:
                       self._exit()
                    case pygame.KEYDOWN:
                        is_key_hold = True
                        if event.key == pygame.K_ESCAPE:
                            self._exit()
                        break
                    case pygame.KEYUP:
                        is_key_hold = False
                        break
            self.surface.fill(color=colors.KORMA)
            self._keypressed(keys= pygame.key.get_pressed(), is_keydown_hold= is_key_hold)
            self._update()
            self._draw()
            pygame.display.update()
            clock.tick(60) # 60 FPS


