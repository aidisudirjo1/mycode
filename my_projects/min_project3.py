

print("What Pokemon suits you by your birth month?")

month = int(input("Enter birth month (1-12): "))

if month == 12:
    assigned_pokemon = 'Abra'
elif month == 1:
    assigned_pokemon = 'Meowth'
elif month == 2:
    assigned_pokemon = 'Balbasaur'
elif month == 3:
    assigned_pokemon = 'Squirtle' 
elif month == 4:
    assigned_pokemon = 'Pikachu'
elif month == 5:
    assigned_pokemon = 'Charmander'
elif month == 6:
    assigned_pokemon = 'Cubone'
elif month == 7:
    assigned_pokemon = 'Psyduck'
elif month == 8:
    assigned_pokemon = 'Ditto'
elif month == 9:
    assigned_pokemon = 'Snorlax'
elif month == 10:
    assigned_pokemon = 'Gastly'
elif month == 11:
    assigned_pokemon = 'Pidgey'

print("Your starter is:", assigned_pokemon)

