from dataclasses import dataclass
from pygame import surface, rect
from draw import draw_ball
from shared.constants import speed, sizes
import entity
from shared.constants.msg_key import MsgKey

@dataclass
class Ball:
    surface: surface.Surface
    layout: rect.Rect
    court_layout: rect.Rect

    def render(self) -> None:
        draw_ball(surface= self.surface, layout= self.layout)

    def update(self) -> None:
        court_limit: float = self._create_circle_point(point_pos= self.court_layout.width, number_of_border_width= 2) / 2
        self.layout = self.layout.move(-speed.BALL_SPEED, 0)
        # layout uses standard coordinates so (0,0) starts at the center
        if self.layout.x < -court_limit or self.layout.x > court_limit:
            if self.layout.x < -court_limit:
                entity.msg_bus.send(key=MsgKey.SCORE, value=entity.player_1.get_type())
            
            if self.layout.x > court_limit:
                entity.msg_bus.send(key=MsgKey.SCORE, value=entity.player_2.get_type())

            self.layout = self._reset_layout()

    def _reset_layout(self) -> rect.Rect:
        return rect.Rect(
            self._create_circle_point(self.court_layout.left),
            self._create_circle_point(self.court_layout.top),
            self._create_circle_point(self.court_layout.width),
            self._create_circle_point(self.court_layout.height))
    
    def _create_circle_point(self, point_pos: int, number_of_border_width: float = 1) -> float:
        return point_pos - (sizes.BALL_RADIUS * number_of_border_width)
