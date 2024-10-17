import os
from lib.utils import Path, GameResult, Gamemode, GameSetting
import json

class ApplicationConfiguration:
    def checkDirectoryExist(self):
        if os.path.isdir(Path().dir_bin):
            pass
        else:
            os.mkdir(Path().dir_bin)
            os.mkdir(Path().dir_config)
            os.mkdir(Path().dir_record)
    
    def create_json_game_statistic(self):
        if os.path.isfile(Path().json_game_statistic):
            return
        
        with open(Path().json_game_statistic, 'w') as file:
            default_setting = {
                Gamemode.Classic.name : {GameResult.WIN.name : 0,
                                         GameResult.LOSE.name : 0},
                Gamemode.Challeng.name : {GameResult.WIN.name : 0,
                                         GameResult.LOSE.name : 0},
                Gamemode.NoTimeLeft.name : {GameResult.WIN.name : 0,
                                         GameResult.LOSE.name : 0}
            }
            json.dump(default_setting, file, indent = 4)
    
    def create_json_game_setting(self):
        if os.path.isfile(Path().json_game_setting):
            return
        
        with open(Path().json_game_setting, 'w') as file:
            default_setting = {
                Gamemode.Classic.name : {GameSetting.Bomb_Time_Min.name : 2,
                                         GameSetting.Bomb_Time_Max.name : 30},
                Gamemode.Challeng.name : {GameSetting.Bomb_Time_Min.name : 2,
                                          GameSetting.Bomb_Time_Max.name : 30},
                Gamemode.NoTimeLeft.name : {GameSetting.Bomb_Time_Min.name : 2,
                                            GameSetting.Bomb_Time_Max.name : 30}
            }
            json.dump(default_setting, file, indent = 4)