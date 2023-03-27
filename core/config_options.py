from shared.interfaces.iyamlconfig import IYAMLConfig
from shared.constants.player_type import PlayerType
from shared.types.size import Size
from shared.configs.custom_yaml_config import CustomYAMLConfig
from shared.configs.default_yaml_config import DefaultYAMLConfig
import yaml

def get_config() -> IYAMLConfig:
    # ALL FIELDS ARE REQUIRED for it to be use in the game
    try:
        with open(r'./config.yml') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
            return CustomYAMLConfig(
                window= Size(width = config['window']['width'], height= config['window']['height']), 
                player_name= config['player']['name'], 
                player_type= PlayerType(config['player']['type']))
    except:
        return DefaultYAMLConfig()

options: IYAMLConfig = get_config()