#!/usr/bin/python


import random


print("I am the last Elite Four, Lets Battle!")

# Define a list of valid choices
choices = ["fire", "water", "grass", "electric", "ground", "poison", "psychic"]

# Prompt the user for their choice
user_choice = input("Choose your Pokemon type:").lower()

# Check if the user's choice is valid
if user_choice not in choices:
    print("Invalid choice. Please try again.")
else:
    # Generate a random choice for the computer
    computer_choice = random.choice(choices)

    # Print the choices
    print(f"You chose {user_choice}, and the computer chose {computer_choice}.")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")

    elif user_choice == "fire" and computer_choice == "grass", "electric", "poison":
        or user_choice == "water" and computer_choice == "fire":
        or user_choice == "grass" and computer_choice == "water", "psychic", "grass":
        or user_choice == "electric" and computer_choice == "water", "posion":
        or user_choice == "ground" and computer_choice == "electric":
        or user_choice == "poison" and computer_choice == "psychic":
        or user_choice == "psychic" and computer_choice == "grass":
     print("You win!")
    
    else:
        print("Computer wins!")



