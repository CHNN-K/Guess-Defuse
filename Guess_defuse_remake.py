import random
import sys
from enum import Enum

class GameResult(Enum):
    WIN = 1,
    LOSE = 2

class Game():
    def __init__(self):
        self.gamemode = None
        self.selectedGamemode = None
        self.gamemode_description = None
        
        self.bombtimeMin = 2
        self.bombtimeMax = 30
        
        self.bombtime = None
        self.remainTime = None
    
        self.lastInput = 0
        self.guessHistory = []
        self.remainTimeHistory = []

        self.firstGuess = False
        
        self.gameResult = None

    def main(self):
        self.Game_Title()
        self.Select_Gamemode()
        self.Defuse(self.Guess())
        self.Game_Result()
        self.Game_End()
    
    def Game_Title(self):
        print ("\n\n")
        print (".================================.")
        print ("|     Defuse the bomb Game       |")
        print (".================================.")

    def Select_Gamemode(self):
        print (">>> Select Game mode <<< ")
        print ("[1]. Classic      : Guess the number to defuse the bomb")
        print ("[2]. Challenge    : For each guess, Bomb time will decrease 1 second")
        print ("[3]. No time left : Guess in 5 Times, Bomb time maximum at 20 seconds")
        print ("[0]. Exit Game")
        gamemode = input("Game mode : ").strip()
        try:
            gamemode = int(gamemode)
            if gamemode < 0 or gamemode > 3:
                print("\n")
                print(">>> Input number out of range")
                print("\n")
                return self.Select_Gamemode()
            
            else:
                if gamemode == 0:
                    sys.exit()
                
                elif gamemode == 1:
                    self.gamemode = self.gamemode_classic
                    self.selectedGamemode = "Classic"
                    self.gamemode_description = "Guess the number to defuse the bomb"
                elif gamemode == 2:
                    self.gamemode = self.gamemode_challenge
                    self.selectedGamemode = "Challenge"
                    self.gamemode_description = "For each guess, Bomb time will decrease 1 second"
                elif gamemode == 3:
                    self.gamemode = self.gamemode_no_time_left
                    self.selectedGamemode = "No time left"
                    self.gamemode_description = "Defuse the bomb in 5 turn, Bomb time maximum at 20 seconds"
                    self.bombtimeMin = 5
                    self.bombtimeMax = 20
                self.Start_Game()
                print(f"\n")
                print(f"Game mode      : {self.selectedGamemode}")
                print(f"Description    : {self.gamemode_description}")
                print(f"================================")
        except:
            print("\n")
            print(">>> Error. Please try again")
            print("\n")
            return self.Select_Gamemode()
    
    def Game_Result(self):
        print("\n")
        print(f"Game result")
        print(f"================================")
        print(f"You {self.gameResult.name}!")
        print(f"Game mode : {self.selectedGamemode}")
        print(f"Bomb time : {self.bombtime}")
        print(f"Your guess {len(self.guessHistory)} times : {self.guessHistory}")
    
    def Game_End(self):
        print("\n")
        print(">>> Play agian? <<<")
        print("[y] : Select Game mode")
        print("[anykey] : End Game")
        try:
            x = input("Command : ").strip().lower()
            if x == "y":
                return self.main()
            else:
                return
        except:
            print("\n")
            print(">>> Error. Please try again")
            print("\n")
            return self.Game_End()
    
    def Start_Game(self):
        self.bombtime = random.randint(self.bombtimeMin, self.bombtimeMax)
        self.remainTime = self.bombtime
        
        self.firstGuess = False
        self.lastInput = 0
        self.guessHistory = []
        self.gameResult = None
    
    
    def Defuse(self, guess : int):
        if not self.firstGuess:
            self.checkFirstGuess(guess)
            self.firstGuess = True
        
        self.remainTime -= guess
        self.gamemode()
    
    def Guess(self):
        x = input("Guess number [1-9] : ").strip()
        print ("\n")
        
        try:
            x = int(x)
            if x <= 0 or x > 9:
                print(">>> Input number out of range")
                print("\n")
                return self.Defuse(self.Guess())
                
            elif x == self.lastInput:
                print(">>> Can't insert same number. Please try agian")
                print("\n")
                return self.Defuse(self.Guess())
            
            else:
                self.lastInput = x
                self.guessHistory.append(x)
                return x
        except:
            print(">>> Error. Please try again")
            print("\n")
            return self.Defuse(self.Guess())
    
    
    def gamemode_classic(self):
        if self.remainTime < 0:
            print("Oh shit! Boom!!!!!!!")
            self.gameResult = GameResult.LOSE
        
        elif self.remainTime == 0:
            self.gameResult = GameResult.WIN

        else:
            self.checkBombStatus()
            self.Defuse(self.Guess())
    
    
    def gamemode_challenge(self):
        if self.remainTime < 0:
            print("Oh shit! Boom!!!!!!!")
            self.gameResult = GameResult.LOSE
        
        elif self.remainTime == 0:
            self.gameResult = GameResult.WIN

        else:
            self.remainTime -= 1
            
            if self.remainTime <= 0:
                print("Beep! Beep! Beep! Boom!!!!!!!")
                self.gameResult = GameResult.LOSE
            
            else:
                self.checkBombStatus()
                self.Defuse(self.Guess())
    
    
    def gamemode_no_time_left(self):
        if self.remainTime < 0:
            print("Oh shit! Boom!!!!!!!")
            self.gameResult = GameResult.LOSE
        
        elif self.remainTime == 0:
            self.gameResult = GameResult.WIN
        
        elif len(self.guessHistory) >= 5:
            print("Time up!!!")
            self.gameResult = GameResult.LOSE

        else:
            self.checkBombStatus()
            self.Defuse(self.Guess())
    
    
    def checkFirstGuess(self, guess : int):
        if guess > self.bombtime:
            while guess > self.bombtime:
                self.bombtime = random.randint(self.bombtimeMin, self.bombtimeMax)
            self.remainTime = self.bombtime
    
    def checkBombStatus(self):
        if (self.remainTime < self.bombtime * (1/3)):
            print ("Bomb status : Red")
        elif (self.remainTime < self.bombtime * (2/3)):
            print ("Bomb status : Yellow")
        else:
            print ("Bomb status : Green")

game = Game()
game.main()