import random


print("I am the last Elite Four, Lets Battle!")

choices = ["fire", "water", "grass", "electric", "posion", "psychic"]

rules = {
    "fire": ["grass", "posion", "electric"],
    "water": ["fire"],
    "grass": ["water", "electric"],
    "electric": ["water", "fire" "poison"],
    "posion": ["grass", "psychic" "water"],
    "psychic": ["grass", "electric" "water"],
    }

player_choice = input("Choose your Pokemon type : ").lower()

if player_choice not in choices:
    print("Invalid choice. Please choose between fire, water, grass, electric, posion, psychic types. ")
else:

    computer_choice = random.choice(choices)
    
    print("You chose:", player_choice)
    print("I chose:", computer_choice)
    

    if player_choice == computer_choice:
        print("It's a tie!")
    elif computer_choice in rules[player_choice]:
        print("You win!")
    else:
        print("I win!")

