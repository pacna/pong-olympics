from core.engine import Engine
import pygame

def main() -> None:
    pygame.init()
    pygame.font.init()
    engine: Engine = Engine()
    engine.run()


if __name__ == "__main__":
    main()