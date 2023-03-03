import pygame
from shared.configs.game_config import GameConfig
from shared import entity
from shared.constants import colors
from shared.types.size import Size
from world import world

class Engine:
    def __init__(self, config: GameConfig) -> None:
        self.config = config
        self.surface = pygame.display.set_mode(size = (self.config.width, self.config.height))

    def run(self) -> None:
        self._load()
        self._run_game()

    def _load(self) -> None:
        pygame.display.set_caption(self.config.title)
        world.load_world(surface= self.surface, screen_size= Size(width= self.config.width, height= self.config.height))

    def _update(self) -> None:
        ...

    def _keypressed(self, key: int, is_keydown_hold: bool) -> None:
        if is_keydown_hold:
            entity.player_1.update(key = key)
            entity.player_2.update(key = key)
            

    def _draw(self) -> None:
        entity.court.render()
        entity.player_1.render()
        entity.player_2.render()
        entity.ball.render()
        entity.score_board.render()

    def _exit(self) -> None:
        pygame.quit()
        quit() # to properly quit out of the program

    def _run_game(self) -> None:
        clock: pygame.time.Clock = pygame.time.Clock()
        is_key_hold: bool = False
        current_key: int = -1
        while True:
            for event in pygame.event.get():
               match event.type:
                    case pygame.QUIT:
                       self._exit()
                    case pygame.KEYDOWN:
                        is_key_hold = True
                        current_key = event.key
                        if event.key == pygame.K_ESCAPE:
                            self._exit()
                        break
                    case pygame.KEYUP:
                        is_key_hold = False
                        current_key = event.key
                        break
            self.surface.fill(color=colors.KORMA)
            self._keypressed(key= current_key, is_keydown_hold= is_key_hold)
            self._draw()
            pygame.display.update()
            clock.tick(60) # 60 FPS


