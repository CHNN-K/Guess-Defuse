from lib.utils import ApplicationConfiguration, GameResult, Gamemode, Path
import json
import math

class Game_Statistic:
    def  __init__(self):
        self.json_data = None
        self.record_classic = []
        self.record_challenge = []
        self.record_notimeleft = []
        
    def winrate_all(self):
        win = self.record_classic[0] + self.record_challenge[0] + self.record_notimeleft[0]
        lose = self.record_classic[1] + self.record_challenge[1] + self.record_notimeleft[1]
        winrate = Game_Statistic.percentage(win, lose)
        return f"{winrate}%"

    def winrate_classic(self):
        win = self.record_classic[0]
        lose = self.record_classic[1]
        winrate = Game_Statistic.percentage(win, lose)
        return f"{winrate}%"

    def winrate_challenge(self):
        win = self.record_challenge[0]
        lose = self.record_challenge[1]
        winrate = Game_Statistic.percentage(win, lose)
        return f"{winrate}%"
    
    def winrate_notimeleft(self):
        win = self.record_notimeleft[0]
        lose = self.record_notimeleft[1]
        winrate = Game_Statistic.percentage(win, lose)
        return f"{winrate}%"
    
    @staticmethod
    def percentage(win, lose):
        if win + lose != 0:
            return round((win / (win + lose)) * 100, 2)
        else:
            return 0
    
    def json_read_record(self):
        try:
            with open(Path().json_game_statistic, 'r') as file:
                self.json_data = json.load(file)
            self.record_classic = [self.json_data[Gamemode.Classic.name][GameResult.WIN.name], self.json_data[Gamemode.Classic.name][GameResult.LOSE.name]]
            self.record_challenge = [self.json_data[Gamemode.Challeng.name][GameResult.WIN.name], self.json_data[Gamemode.Challeng.name][GameResult.LOSE.name]]
            self.record_notimeleft = [self.json_data[Gamemode.NoTimeLeft.name][GameResult.WIN.name], self.json_data[Gamemode.Classic.name][GameResult.LOSE.name]]
        except:
            print ("Can't find record json")