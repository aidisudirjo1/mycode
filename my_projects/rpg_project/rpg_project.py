#!/usr/bin/python3


import os

# Display starting menu
def prompt():
    print("\t\tWelcome to my game\n\n\
You must collect all six items before fighting the Zombies outside.\n\n\
Moves:\t'go {direction}' (travel north, south, east, or west)\n\
\t'get {item}' (add nearby item to inventory)\n")

    input("Press any key to continue...")


# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Map
rooms = {
    'Kitchen': {'North': 'Bathroom', 'South': 'Bedroom', 'East': 'Living Room'},
    'Bathroom': {'South': 'Kitchen', 'Item': 'Bullets'},
    'Bedroom': {'North': 'Kitchen', 'Item': 'Guns'},
    'Living Room' : {'West': 'Kitchen', 'East': 'Outside', 'Item': 'Machete'},
    'Outside': {'West': 'Bazaar', 'Boss': 'the Zombies'}
    }

# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# List to track inventory
inventory = []

# Tracks current room
current_room = "Kitchen"

# Tracks last move
msg = ""

clear()
prompt()

# Gameplay loop
while True:

    clear()

    # Display player info
    print(f"You are in the {current_room}\nInventory : {inventory}\n{'-' * 27}")

    # Display msg
    print(msg)

    # Item indicator
    if "Item" in rooms[current_room].keys():

        nearby_item = rooms[current_room]["Item"]

        if nearby_item not in inventory:

            if nearby_item[-1] == 's':
                print(f"You see {nearby_item}")

            elif nearby_item[0] in vowels:
                print(f"You see an {nearby_item}")

            else:
                print(f"You see a {nearby_item}")
    
    # Boss encounter
    if "Boss" in rooms[current_room].keys():

        if len(inventory) < 3:
            print(f"You lost a fight with {rooms[current_room]['Boss']}.")
            break

        else:
            print(f"You beat {rooms[current_room]['Boss']}!")
            break

    # Accepts player's move as input
    user_input = input("Enter your move:\n")

    # Splits move into words
    next_move = user_input.split(' ')

    # First word is action
    action = next_move[0].title()

    # Reset item and direction
    item = "Item"
    direction = "null"

    # Second word is object or direction
    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = " ".join(item).title()

    # Moving between rooms
    if action == "Go":

        try:
            current_room = rooms[current_room][direction]
            msg = f"You travel {direction}"

        except:
            msg = "You can't go that way."
    
    # Picking up items
    elif action == "Get":
        try:
            if item == rooms[current_room]["Item"]:

                if item not in inventory:

                    inventory.append(rooms[current_room]["Item"])
                    msg = f"{item} retrieved!"

                else:
                    msg = f"You already have the {item}"
            
            else:
                msg = f"Can't find {item}"
        except:
            msg = f"Can't find {item}"
    
    # Exit program
    elif action == "Exit":
        break

    # Any other commands invalid
    else:
        msg = "Invalid command"
