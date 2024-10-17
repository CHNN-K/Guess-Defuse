from enum import Enum

class GameResult(Enum):
    WIN = 1,
    LOSE = 2

class Gamemode(Enum):
    Classic = 1,
    Challeng = 2,
    NoTimeLeft = 3

class GameSetting(Enum):
    Bomb_Time_Min = 1,
    Bomb_Time_Max = 2,

class BombStatus(Enum):
    GREEN = 1,
    YELLOW = 2,
    RED = 3,
    DEFUSED = 4,
    EXPLODE = 5