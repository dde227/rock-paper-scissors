# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

print("USER CHOICE: ", user_choice)



if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissor"):
    print("VALID USER CHOISE. KEEP GOING.")
else:    
    print("OOPS, INVALID INPUT. PLEASE TRY AGAIN.")
    exit()

valid_options = ["rock","paper","scissor"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE: ",computer_choice)

print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")