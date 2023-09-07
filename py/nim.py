# nim.py
# Andy Mina
# CSCI 77800 Fall 2023
import random

def getPlayerMove(totalStones: int) -> int:
    print('Enter # of stones to rmeove (1-3): ', end='')
    validMove: bool = False
    playerStones: int = 0

    while (not validMove):
        try:
            playerStones = int(input())
            inValidRange: bool = 1 <= playerStones <= 3
            canBeRemoved: bool = totalStones - playerStones >= 0
            validMove = inValidRange and canBeRemoved

            if (not validMove):
                print('Number must be in the range 1-3: ', end='')
        except:
            print('Number was not an int.')
    
    return playerStones

def getCPUMove(totalStones: int) -> int:
    return totalStones if (totalStones <= 3) else random.randint(1, 3)

def playNim() -> None:
    totalStones: int = 12
    winner: string = 'CPU'

    while (totalStones != 0 and winner != 'Player'):
        print(totalStones + ' stones remain.')
        totalStones -= getPlayerMove(totalStones)
        
        if (totalStones == 0):
            winner = 'Player'
        else:
            cpuMove: int = getCPUMove(totalStones)
            totalStones -= cpuMove
            print('CPU removed ' + ' stones.')

    print("🎉 " + winner + " removed the last stone! 🎉");

def shouldRestart() -> bool:
    print('Play again? Enter y/n: ', end='')

    while (True):
        letter: str = input()

        if (letter == 'y' or letter == 'n'):
            return True
        else:
            print('Enter only "y" or "n": ', end='')

continuePlaying: bool = True
while (continuePlaying):
    playNim()
    continuePlaying = shouldRestart()