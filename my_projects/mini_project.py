import random

def get_player_choice():
    choices = ["fire", "water", "grass", "electric", "poison", "psychic"]
    while True:
        player_choice = input("Choose your Pokemon type: ").lower()
        if player_choice in choices:
            return player_choice
        else:
            print("Invalid choice. Please choose between fire, water, grass, electric, poison, or psychic types.")

def get_computer_choice(choices):
    return random.choice(choices)

def determine_winner(player_choice, computer_choice, rules):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in rules[player_choice]:
        return "You win!"
    else:
        return "I win!"

def play_game():
    print("I am the last Elite Four, Let's Battle!")
    choices = ["fire", "water", "grass", "electric", "poison", "psychic"]
    rules = {
        "fire": ["grass", "poison", "electric"],
        "water": ["fire"],
        "grass": ["water", "electric"],
        "electric": ["water", "fire", "poison"],
        "poison": ["grass", "psychic", "water"],
        "psychic": ["grass", "electric", "water"]
    }
    player_choice = get_player_choice()
    computer_choice = get_computer_choice(choices)
    print("You chose:", player_choice)
    print("I chose:", computer_choice)
    result = determine_winner(player_choice, computer_choice, rules)
    print(result)

play_game()

