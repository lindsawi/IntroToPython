# Rock.py
# Play rock, paper, scissors
# Lindsay Williams 
# Feb 12, 2020

from random import randint

#create a list of play options
c = ["rock", "paper", "scissors"]

#assign a random play to the computer
computer = c[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Do you want to choose rock, paper, or scissors?")
    if player == computer:
        print("Tie! Play again! ")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You won!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("You won!", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You won!", player, "cut", computer)
    else:
        print("What item did you want to choose again?")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = c[randint(0,2)]
