import pygame
from engine.engine import Engine
from shared.configs.game_config import GameConfig


def main() -> None:
    pygame.init()
    pygame.font.init()
    engine: Engine = Engine(config= GameConfig(title='Pygame Pong', height=720, width=1280))
    engine.run()


if __name__ == "__main__":
    main()