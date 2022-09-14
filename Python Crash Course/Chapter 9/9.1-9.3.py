print("Exercise 9.1")
class Restaurant():
    """class for describing a restaurant"""
    def __init__(self, name, cuisine_type):
        """provides name and cuisine type"""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """describes the restaurant"""
        print(f"The restaurant's name is {self.name} and provides"
              f" {self.cuisine_type} style cuisine.")

    def open_restaurant(self):
        """Statement for opening the restaurant"""
        print(f"{self.name} is now open")

restaurant = Restaurant('54', 'Asian')
print(f"Let's check out {restaurant.name} because I heard they have"
      f" fantastic {restaurant.cuisine_type} food")

restaurant.describe_restaurant()

print("\nExercise 9.2")
pizza = Restaurant('Dominos', 'italian')
pizza.describe_restaurant()
pizza.open_restaurant()

sushi = Restaurant('Itachi', 'japanese')
sushi.describe_restaurant()
sushi.open_restaurant()

print("\nExercise 9.3")
class User:
    """Create a user class"""
    def __init__(self, first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Use to describe a user base"""
        print(f'{self.first_name} {self.last_name}')

    def greet_user(self):
        """Greets the user"""
        print(f"Just wanted to wish {self.first_name.title()} {self.last_name.title()}"
              f" a happy holiday!")

my_self = User('BrIAn', 'dy')
my_self.describe_user()
my_self.greet_user()

your_self = User('tiffany', 'wong')
your_self.describe_user()
your_self.greet_user()