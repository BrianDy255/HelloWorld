#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.

import art
import random
print(art.logo)

#sets the amount of "tries" a person has to guess the number.
count = 0

#A function to allow the user to have option to play again
def play_again():
    play = input("Would you like to play again? Type 'y' or 'n':\n")
    if play == 'y':
        number_guessing_game()
    else:
        print("That is not a valid response. Try Again\n")
        play_again()

def number_guessing_game():
    #generate a random number between 1-100 using the randint function.
    random_number = random.randint(1,100)
    #Set the difficulty for the game. (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
    difficulty = int(input("Select Difficulty:\n 1. Easy (10 tries) \t2. Difficult (5 tries): \n"))
    if difficulty == 1:
        count = 10
    else:
        count = 5
    user_guess = ""
    while random_number != user_guess:
        user_guess = int(input("Guess a number between 1 - 100:\n"))
        if random_number > user_guess:
            print("Guess HIGHER")
            count -= 1
            print(f'Current count: {count}')
        elif random_number < user_guess:
            print("Guess LOWER")
            count -= 1
            print(f'Current count: {count}')
        if count == 0:
            print("You have no more tries left. \n")
            play_again()
        elif random_number == user_guess:
            print("You Guessed Correctly!\n")

    play_again()

number_guessing_game()