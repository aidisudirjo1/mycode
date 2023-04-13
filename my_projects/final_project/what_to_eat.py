import random

# Define a dictionary of cuisines and corresponding restaurants
cuisine_restaurants = {
    'italian': ['Pasta Bella', 'Mamma Mia', 'La Piazza'],
    'mexican': ['Taco Loco', 'El Mariachi', 'La Taqueria'],
    'japanese': ['Sushi Train', 'Tokyo Grill', 'Trappers'],
    'american': ['Buffalo Wild Wing', 'Red Robin', 'Applebee\'s'],
    'indian': ['Curry Corner', 'Curry House', 'Indian Cuisine'],
    'thai': ['Thai Spice', 'Siam Orchid', 'Bangkok Bistro']
}

# Prompt the user for their preferred cuisine
user_cuisine = input("What cuisine do you prefer? ").lower()

# Check if the user's preferred cuisine is in the dictionary
if user_cuisine in cuisine_restaurants:
    # If it is, select a random restaurant from the corresponding list
    selected_restaurant = random.choice(cuisine_restaurants[user_cuisine])
    print(f"Based on your preference for {user_cuisine}, we recommend: {selected_restaurant}")
else:
    # If it's not, let the user know and suggest a random restaurant from the entire list
    print(f"Sorry, we don't have any {user_cuisine} restaurants on our list.")
    all_restaurants = [restaurant for restaurants in cuisine_restaurants.values() for restaurant in restaurants]
    selected_restaurant = random.choice(all_restaurants)
    print(f"However, we recommend: {selected_restaurant}")

