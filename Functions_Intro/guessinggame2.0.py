import random


def get_integer(prompt):
    """
    Gets an integer from Standard Input (stdin).

    The function will continue looping, and prompting the user,
    until a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print(f"Please enter a numerical value between 1,{highest}")

print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)

highest = 100
answer = random.randint(1,highest)
print(answer)

print("Please guess a number between 1 and {}".format(highest))
guess = None

while answer != guess:
    guess = get_integer(": ")
    if guess == 0:
        print("QUITTNG")
        break
    if guess == answer:
        print("well done you guessed it")
    else:
        if guess < answer:
            print("Guess higher")
        else:
            print("Guess lower")