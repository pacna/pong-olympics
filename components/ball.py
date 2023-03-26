from dataclasses import dataclass
from typing import Callable
from pygame import surface, rect
from draw import draw_ball
from shared.constants import speed, sizes
import entity
from shared.constants.msg_key import MsgKey
from shared.types.position import Position

@dataclass
class Ball:
    surface: surface.Surface
    layout: rect.Rect
    court_layout: rect.Rect
    player_1_layout: rect.Rect
    player_2_layout: rect.Rect
    x_velocity: float = speed.BALL_SPEED
    y_velocity: float = speed.BALL_SPEED

    def render(self) -> None:
        draw_ball(surface= self.surface, layout= self.layout)

    def update(self) -> None:
        court_top, court_bottom, court_left, court_right = (
            self.court_layout.top + sizes.GAME_COURT_BORDER_WIDTH, 
            self.court_layout.bottom - sizes.GAME_COURT_BORDER_WIDTH, 
            self.court_layout.left + sizes.GAME_COURT_BORDER_WIDTH, 
            self.court_layout.right - sizes.GAME_COURT_BORDER_WIDTH )

        updated_layout: rect.Rect = self.layout.move(self.x_velocity, self.y_velocity)

        if updated_layout.colliderect(self.player_1_layout):
            self.y_velocity *= -1.05
            self.x_velocity = -self.x_velocity
            updated_layout = self.layout.move(speed.BALL_SPEED, self.y_velocity)

        if updated_layout.colliderect(self.player_2_layout):
            self.y_velocity *= -1.05
            self.x_velocity = self.x_velocity
            updated_layout = self.layout.move(speed.BALL_SPEED, self.y_velocity)

        if updated_layout.y < court_top or updated_layout.y > court_bottom:
            self.y_velocity *= -1.05
            updated_layout = self.layout.move(speed.BALL_SPEED, self.y_velocity)

        if updated_layout.x < court_left or updated_layout.x > court_right:
            if updated_layout.x < court_left:
                entity.msg_bus.send(key=MsgKey.SCORE, value=entity.player_1.get_type())
                self.x_velocity = -self.x_velocity
            
            if updated_layout.x > court_right:
                entity.msg_bus.send(key=MsgKey.SCORE, value=entity.player_2.get_type())
                self.x_velocity = self.x_velocity

            updated_layout = self._reset_layout()

        self.layout = updated_layout

    def _reset_layout(self) -> rect.Rect:
        create_circle_point: Callable[[int], float] = lambda xy: xy - (sizes.GAME_COURT_BORDER_WIDTH * 2)
        ball_pos: Position = Position(x = create_circle_point(entity.court.layout.centerx), y = entity.court.layout.centery - create_circle_point(sizes.GAME_COURT_BORDER_WIDTH * 2))
        return rect.Rect(
            ball_pos.x,
            ball_pos.y,
            sizes.BALL_HEIGHT_WIDTH,
            sizes.BALL_HEIGHT_WIDTH)
