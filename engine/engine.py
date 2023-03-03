import pygame
from components.score_board import draw_score_board
from pieces import pieces
from shared.constants import colors
from engine.types.engine_config import EngineConfig
from shared.types.size import Size
from world import world

class Engine:

    def __init__(self, config: EngineConfig) -> None:
        self.config = config
        self.surface = pygame.display.set_mode(size = (self.config.width, self.config.height))

    def run(self) -> None:
        self._load()
        draw_score_board(game_surface = self.surface)

        self._run_game()

    def _load(self) -> None:
        pygame.display.set_caption(self.config.title)
        self.surface.fill(color=colors.KORMA)
        world.load_world(surface= self.surface, screen_size= Size(width= self.config.width, height= self.config.height))

    def _update(self) -> None:
        ...

    def _keypressed(self, key: int, is_keydown_hold: bool) -> None:
        if is_keydown_hold:
            pieces.player_1.update(key = key)
            pieces.player_2.update(key = key)
            

    def _draw(self) -> None:
        pieces.court.render()
        pieces.player_1.render()
        pieces.player_2.render()

    def _exit(self) -> None:
        pygame.quit()
        quit() # to properly quit out of the program

    def _run_game(self) -> None:
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
            self._keypressed(key= current_key, is_keydown_hold= is_key_hold)
            self._draw()
            pygame.display.update()


