#Python 3 Rock, Paper Scissors

import random

 #a list of options for game

options = ["rock", "paper", "scissors"]

#Input messsage (Direction for user)

user_choice = input("Choose rock, paper, or scissors: ")

computer_choice = random.choice(options)

 #prints out message of what you chose and computer chose

print("You chose: ", user_choice)

print("Computer chose: ", computer_choice)


#LOWERCASE VERSION (describes Tie between Rock, Paper and Scissors)

if user_choice == computer_choice:

    print("It's a tie!")

#Rock vs anything

elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")

elif user_choice == "rock" and computer_choice == "paper":
    print("Computer wins!")

#paper vs anything

elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")

elif user_choice == "paper" and computer_choice == "scissors":
    print("Computer wins")

#scissors vs anything

elif user_choice == "scissors" and computer_choice == "paper":
    print("You Win!")

elif user_choice == "scissors" and computer_choice == "rock":
    print("Computer wins!")
