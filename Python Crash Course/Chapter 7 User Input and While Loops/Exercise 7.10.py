responses = {}

active = True

while active:
    name = input("What's your name?\n")
    place = input("What is your dream vacation? \n")

    responses[name] = place.lower()

    repeat = input("Would you like to add anybody else? Yes / No").lower()
    if repeat == 'no':
        break

for name, favorite in responses.items():
    print(f"{name} wish list to go is {favorite}")