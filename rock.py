# Rock.py
# Play rock, paper, scissors
# Lindsay Williams 
# Feb 25, 2020

from random import randint

#create a list of play options
c = ["rock", "paper", "scissors"]

#assign a random play to the computer
computer = c[randint(0,2)]

#set player to False
player = False

while player == False:
#set true rock, paper, scissors statements
    player = input("Do you want to choose rock, paper, or scissors?")
    if player == computer:
        print("tie! rematch! ")
    elif player == "rock":
        if computer == "paper":
            print("you lose!", computer, "covers", player)
        else:
            print("you won!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("you lose!", computer, "cuts", player)
        else:
            print("You won!", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("you lose!", computer, "smashes", player)
        else:
            print("you won!", player, "cuts", computer)
    else:
        print("What item did you want to choose again?")
    #player was set to True, but want it to be False so loop continues
    player = False
    computer = c[randint(0,2)]
