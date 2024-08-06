import asyncio
from core.engine import Engine
import pygame

async def main() -> None:
    pygame.init()
    pygame.font.init()
    engine: Engine = Engine()
    await engine.run()


if __name__ == "__main__":
    asyncio.run(main())