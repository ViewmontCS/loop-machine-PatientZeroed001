from random import randint
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#variables
playerScore = 1500
costOfPlaying = 15.00
pointsPerWin = 50.00
win = 50.00
slots = [[1,2,3],[4,5,6],[7,8,9]]
#start
print("Welcome to the Game!")
print("You start with a score of", playerScore)
print("Each time you play, it will cost you", costOfPlaying, "points.")
print("Good luck!")
#start game
while True:
    play_input = input(f"\nPress Enter to play again (cost: {costOfPlaying} points), or type 'q' to quit: ")
    if play_input.lower() == 'q':
            break
    if playerScore < costOfPlaying:
        print("Sorry, you do not have enough points to play again.")
        break

    for i in range(10):
     for row in slots:
        for j in range(len(row)):
            row[j] = randint(1,9)
    clear()
    for row in slots:
        for num in row:
            print(f"|{num}|",end="")
        print()

#end
    if slots[0][0] == slots[0][1] == slots[0][2] or slots[1][0] == slots[1][1] == slots[1][2] or slots[2][0] == slots[2][1] == slots[2][2]:
            print("Congratulations! You won 50 pts!")
            playerScore += win
    elif slots[0][0] == slots[1][1] == slots[2][2] or slots[0][2] == slots[1][1] == slots[2][0]:
            print("Congratulations! You won 50 pts!")
            playerScore += win
    else:
        print("Sorry, you lost this round.")
        playerScore -= costOfPlaying

    print("Your final score is:", playerScore)