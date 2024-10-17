import os
import sys

class Path:
    def __init__(self):
        self.dir_bin = "bin"
        self.dir_config = "bin/config"
        self.dir_record = "bin/record"
        self.json_game_statistic = "bin/record/game_statistic.json"
        self.json_game_setting = "bin/config/game_setting.json"
        
    def resource_path(self, path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, path)