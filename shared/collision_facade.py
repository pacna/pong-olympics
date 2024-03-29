from dataclasses import dataclass
from shared.constants.msg_key import MsgKey
from shared.constants import sizes,speed
import core.entity as entity

@dataclass
class CollisionFacade:
    def collide(self) -> None:
        court_top, court_bottom, court_left, court_right = (
            entity.court.layout.top + sizes.GAME_COURT_BORDER_WIDTH, 
            entity.court.layout.bottom - sizes.GAME_COURT_BORDER_WIDTH, 
            entity.court.layout.left + sizes.GAME_COURT_BORDER_WIDTH, 
            entity.court.layout.right - sizes.GAME_COURT_BORDER_WIDTH )
        
        # wall collision logic
        if entity.ball.layout.y < court_top or entity.ball.layout.y > court_bottom:
            entity.ball.y_velocity *= -speed.VELOCITY_MULTIPLIER
            entity.ball.layout = entity.ball.layout.move(entity.ball.x_velocity, entity.ball.y_velocity)

        if entity.ball.layout.x < court_left or entity.ball.layout.x > court_right:
            if entity.ball.layout.x < court_left:
                entity.msg_bus.send(key=MsgKey.SCORE, value=entity.player_2.get_name())
            
            if entity.ball.layout.x > court_right:
                entity.msg_bus.send(key=MsgKey.SCORE, value=entity.player_1.get_name())

            entity.ball.layout = entity.ball.reset_pos()
            entity.ball.x_velocity = entity.ball.reset_velocity(entity.ball.x_velocity)
            entity.ball.y_velocity = entity.ball.reset_velocity(entity.ball.y_velocity) 

        # players collision logic
        if entity.ball.layout.colliderect(entity.player_1.get_layout()) or entity.ball.layout.colliderect(entity.player_2.get_layout()):
            entity.ball.y_velocity *= -speed.VELOCITY_MULTIPLIER
            entity.ball.x_velocity = -entity.ball.x_velocity
            entity.ball.layout = entity.ball.layout.move(entity.ball.x_velocity, entity.ball.y_velocity)

