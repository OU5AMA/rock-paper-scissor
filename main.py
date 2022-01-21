from operator import truediv
from random import choice

option = ["rock", "paper", "scissor"]
computer = choice(option)
player = None

while player not in option:
    player = input("choose either: (rock, paper, or scissor): ")
    player = player.strip()
    player = player.lower()
    print("PLEASE! write your answer first 😐")if player == "" else print(f"computer == {computer} \nplayer == {player}" )

    if player == computer:
        print("Tie!! ")
    elif player == "rock":
        print("You win ") if computer == "scissor" else print("you lose")
    elif player == "paper":
        print("You win ") if computer == "paper" else print("you lose")
    elif player == "scissor":
        print("You win ") if computer == "rock" else print("you lose")
    else:
        print("PLEASE, CHOOSE ONE OF THE GIVEN OPTIONS.")

