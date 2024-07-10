import random
import json

bombtimeMin = 2
bombtimeMax = 30
bombtime = random.randint(bombtimeMin, bombtimeMax)
remainTime = bombtime

lastInput = 0
inputHistory = []
remainTimeHistory = []

isPlay = True
isEnd = False
isStart = False
firstGuess = False

def defuseBomb(time):
    global bombtime, remainTime, isEnd, isPlay
    
    if (time != 0):
        remainTime -= time
        inputHistory.append(int(x))
        
    if (remainTime == 0):
        print ("Bomb has been defused")
        print ("You Win!!!\n")
        
        print (f"Bomb time = {bombtime}")
        print (f"Your move = {inputHistory}")
        print (f"Remaintime = {remainTimeHistory}")
        
        isPlay = False
        isEnd = True
        
        with open("Log/Record.json", "r") as record:
            newRecord = json.load(record)
        newRecord["Win"] += 1
        with open("Log/Record.json", "w") as newfile:
            json.dump(newRecord, newfile, indent = 10)
            
        print(newRecord)
        return
    
    if (time != 0):
        remainTime -= 1
        remainTimeHistory.append(remainTime)
    
    if (remainTime <= 0):
        print ("Boom!!!")
        print ("Game Over\n")
        
        print (f"Bomb time = {bombtime}")
        print (f"Your move = {inputHistory}")
        print (f"Remaintime = {remainTimeHistory}")
        
        isPlay = False
        isEnd = True
        
        with open("Log/Record.json", "r") as record:
            newRecord = json.load(record)
        newRecord["Lose"] += 1
        with open("Log/Record.json", "w") as newfile:
            json.dump(newRecord, newfile, indent = 10)
            
        print(newRecord)
        return
    
    elif (remainTime < bombtime * (1/3)):
        print ("Bomb status : Red")
    elif (remainTime < bombtime * (2/3)):
        print ("Bomb status : Yellow")
    else:
        print ("Bomb status : Green")

while isEnd != True:
    if (not isStart):
        print ("\n\n")
        print (".================================.")
        print ("|     Defuse the bomb Game       |")
        print (".================================.")
        print ("Guess the number to defuse it!")
        print ("Each Guess will waste bomb time 1 second.\n")
        isStart = True
        
        bombtime = random.randint(bombtimeMin,bombtimeMax)
        remainTime = bombtime
        lastInput = 0
        inputHistory = []
        remainTimeHistory = []
        
    if (isPlay):
        print ("Guess Number (1-9) for Defuse the bomb")
        x = input()
        try:
            if (int(x) > 9 or int(x) < 1):
                print("Input number out of range")
                
            elif (lastInput != int(x) and int(x) > 0):
                if (firstGuess == False and int(x) >= bombtime):
                    while int(x) > bombtime:
                        bombtime = random.randint(bombtimeMin, bombtimeMax)
                    remainTime = bombtime
                    firstGuess = True
                defuseBomb(int(x))
                lastInput = int(x)
                
            elif (lastInput == int(x)):
                print("Can't insert same number. Please try agian")
                defuseBomb(0)
        except:
            print("Error. Please try again")
        print("\n")
        
    if (isEnd):
        print ("Play again? <Y/N>")
        y = input()
        if (y.lower() == "y"):
            isPlay = True
            isEnd = False
            isStart = False
            firstGuess = False
        elif (y.lower() == "n"):
            break
        else:
            print("Input wrong command. Please try agian.\n")