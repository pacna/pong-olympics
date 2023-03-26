from pygame import surface, rect
from mocks.mock_player import MockPlayer
from shared.constants import colors
from shared.constants.player_type import PlayerType
import entity

entity.player_1 = MockPlayer(
    name= "Faker",
    surface= surface.Surface((0, 0)),
    color= colors.WHITE,
    layout= rect.Rect(0, 0, 0, 0),
    type= PlayerType.SELF,
    court_layout= rect.Rect(0, 0, 0, 0)
)

def test_get_player_name() -> None:
    # ARRANGE
    expected_name: str = "Faker"

    # ACT
    name: str = entity.player_1.get_name()

    # ASSERT
    assert(expected_name == name)

def test_get_player_type() -> None:
    # ARRANGE
    expected_type: PlayerType = PlayerType.SELF

    # ACT
    player_type: PlayerType = entity.player_1.get_type()

    # ASSERT
    assert(expected_type == player_type)