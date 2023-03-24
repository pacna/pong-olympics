from dataclasses import dataclass

from pygame import surface

from draw import draw_score_board
from shared.constants.msg_key import MsgKey
from shared.types.key_value_pair import KeyValuePair
from shared.constants.player_type import PlayerType
from shared.types.size import Size


@dataclass
class ScoreBoard:
    surface: surface.Surface
    screen_size: Size
    team_one_score: int = 0
    team_two_score: int = 0

    def render(self) -> None:
        draw_score_board(game_surface= self.surface, screen_size= self.screen_size, team_one_score= self.team_one_score, team_two_score= self.team_two_score)

    def handle_msg(self, msg: KeyValuePair[PlayerType]) -> None:
        if msg.key != MsgKey.SCORE:
            return
        
        if msg.value == PlayerType.SELF:
            self.team_one_score+=1
            return

        self.team_two_score+=1 
        