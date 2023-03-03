from dataclasses import dataclass

@dataclass
class GameConfig:
    title: str
    height: int
    width: int