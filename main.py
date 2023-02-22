import pygame
from engine.engine import Engine
from engine.types.engine_config import EngineConfig


def main() -> None:
    pygame.init()
    pygame.font.init()
    engine: Engine = Engine(config= EngineConfig(title='Pygame Pong', height=720, width=1280))
    engine.run()


if __name__ == "__main__":
    main()