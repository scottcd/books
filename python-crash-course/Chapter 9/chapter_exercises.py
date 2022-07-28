# Restaurant
class Restaurant:
    """A simple class to model a restaurant."""
    
    def __init__(self, resaurant_name, cuisine_type):
        """Initialize the restaurant's name and cuisine."""
        self.restaurant_name = resaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a message that describes the restaurant"""
        print(f"{self.restaurant_name.title()} serves some yummy {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name.title()} is now open!")

brunos = Restaurant("bruno's", "fish sticks")

print(f"{brunos.restaurant_name} is mid at best, and their {brunos.cuisine_type} suck!")
brunos.describe_restaurant()
brunos.open_restaurant()

# Three Restaurants
nestys = Restaurant("nesty's", "pizza")
guys = Restaurant("guy's", "burgers")
frans = Restaurant("fran's", "italian")

nestys.describe_restaurant()
guys.describe_restaurant()
frans.describe_restaurant()

# Users
class User:
    """A simple class to model a user"""

    def __init__(self, first_name, last_name):
        """Initialize a user's name."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"User's name is {self.first_name} {self.last_name}.")

    def greet_user(self):
        """Prints a customized greeting to the user."""
        print(f"Hello, {self.first_name}!")

ron = User("ron", "weasely")
tron = User("tron", "active")
marc = User("marc", "west")
anton = User("anton", "y")

ron.describe_user()
ron.greet_user()
tron.describe_user()
tron.greet_user()
marc.describe_user()
marc.greet_user()
anton.describe_user()
anton.greet_user()