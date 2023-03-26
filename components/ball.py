from dataclasses import dataclass
from typing import Callable
from pygame import surface, rect
from draw import draw_ball
from shared.constants import speed, sizes
from shared.types.position import Position

@dataclass
class Ball:
    surface: surface.Surface
    layout: rect.Rect
    court_layout: rect.Rect
    x_velocity: float = speed.BALL_SPEED
    y_velocity: float = speed.BALL_SPEED

    def render(self) -> None:
        draw_ball(surface= self.surface, layout= self.layout)

    def update(self) -> None:
        self.layout = self.layout.move(self.x_velocity, self.y_velocity)

    def reset_pos(self) -> rect.Rect:
        create_circle_point: Callable[[int], float] = lambda xy: xy - (sizes.GAME_COURT_BORDER_WIDTH * 2)
        ball_pos: Position = Position(x = create_circle_point(self.court_layout.centerx), y = self.court_layout.centery - create_circle_point(sizes.GAME_COURT_BORDER_WIDTH * 2))
        return rect.Rect(
            ball_pos.x,
            ball_pos.y,
            sizes.BALL_HEIGHT_WIDTH,
            sizes.BALL_HEIGHT_WIDTH)
    
    def reset_velocity(self, velocity: float) -> float:
        return -speed.BALL_SPEED if velocity < 0 else speed.BALL_SPEED