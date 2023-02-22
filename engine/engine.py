import pygame
from components.score_board import draw_score_board
from players.player import Player
from players.player_factory import PlayerFactory
from players.types.player_config import PlayerConfig
from players.types.player_type import PlayerType
from shared.constants import colors
from engine.types.engine_config import EngineConfig
from shared.types.position import Position

class Engine:

    def __init__(self, config: EngineConfig) -> None:
        self.config = config
        self.surface = pygame.display.set_mode(size = (self.config.width, self.config.height))

    def run(self) -> None:
        pygame.display.set_caption(self.config.title)
        self.surface.fill(color=colors.KORMA)
        game_court_size: pygame.Rect = pygame.Rect(0, 150, self.config.width, self.config.height - 150)
        pygame.draw.rect(surface = self.surface, color= colors.WHITE, rect= game_court_size, width = 5)

        draw_score_board(game_surface = self.surface)

        PlayerFactory(players=[
            Player(config=PlayerConfig(type=PlayerType.SELF, color=colors.RED_DAMASK, position=Position(x = game_court_size.x + 5, y = game_court_size.y + 5), surface=self.surface)),
            Player(config=PlayerConfig(type=PlayerType.COMPUTER, color=colors.FRUIT_SALAD, position=Position(x = 1270 - 5, y = game_court_size.y + 5), surface=self.surface))
        ]).render()

        self.__run_game()

    def __run_game(self) -> None:
        while True:
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.exit()

    def exit(self) -> None:
        pygame.quit()
        exit() # to properly quit out of the program


