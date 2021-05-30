# game.py

import random
import os
import dotenv

dotenv.load_dotenv()

player_name = os.getenv("PLAYER_NAME")

print("-------------------")
print("Welcome",player_name,"to my Rock-Paper-Scissors game...")
print("-------------------")

user_choice = input("Please choose either 'rock', 'paper', 'scissors': ")

print("You chose: '" + user_choice + "'")

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    
    valid_options = ["rock","paper","scissors"]
    computer_choice = random.choice(valid_options)
    print("The computer chose: '" + computer_choice + "'")
    print("-------------------")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "scissors") and (computer_choice == "paper"):
        print("Hurray, you win!")
    elif (user_choice == "rock") and (computer_choice == "scissors"):
        print("Hurray, you win!")
    elif (user_choice == "paper") and (computer_choice == "rock"):
        print("Hurray, you win!")
    else:
        print("Oh, the computer won. It's ok.")

else:    
    print("-------------------")
    print("Oops, invalid input. Please try again.")
    exit()

print("-------------------")

print("Thanks for playing. Please play again!")