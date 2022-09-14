print("Exercise 8.1")

def display_message():
    """Displays a simple message"""
    print("We are learning about how to create functions"
          "in python")

display_message()

print("\nExercise 8.2")
def favorite_book(title):
    """Accepts a parameter and value to favorite book"""
    print(f'One of my favorite book to read is {title.title()}')

favorite_book('Alice in Wonderland')