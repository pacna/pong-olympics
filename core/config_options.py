import json
from shared.interfaces.igameconfig import IGameConfig
from shared.constants.player_type import PlayerType
from shared.types.size import Size
from shared.configs.custom_game_config import CustomGameConfig
from shared.configs.default_game_config import DefaultGameConfig

def get_config() -> IGameConfig:
    # ALL FIELDS ARE REQUIRED for it to be use in the game
    try:
        with open(r'./config.json', 'r') as file:
            config = json.load(file)
            return CustomGameConfig(
                window= Size(width = config['window']['width'], height= config['window']['height']), 
                player_name= config['player']['name'], 
                player_type= PlayerType(config['player']['type']))
    except:
        return DefaultGameConfig()

options: IGameConfig = get_config()