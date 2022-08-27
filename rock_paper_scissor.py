import random
import os
import re

os.system('cls' if os.name=='nt' else 'clear')

while (1<2):
    print("\n")
    print("Rock, Paper, Scissors")
    userChoice = input("Choose your weapon: [R]ock, [P]aper or [S]cissors: ")
    if not re.match("[SsRrPp]", userChoice):
        print("Please choose a letter: ")
        print("[R]ock, [P]aper or [S]cissors")
        continue

    #echo users choice
    print("You chose: " + userChoice)

    #opponents choice
    choices = ['R', 'P', 'S']
    opponentChoice = random.choice(choices)
    
    if opponentChoice == str.upper(userChoice):
        print("Tie! ")
    
    elif opponentChoice == 'R' and userChoice.upper() == 'S':
        print("Scissor beats Rock, the computer wins!")
        continue

    elif opponentChoice == 'S' and userChoice.upper() == 'P':
        print("Scissors beats Paper, the computer wins! ")
        continue
    
    elif opponentChoice == 'P' and userChoice.upper() == 'R':
        print ("Paper beats Rock, the computer wins!")
        continue
    else:
        print (str(opponentChoice) + " beats " + str(userChoice) + " the player wins!")