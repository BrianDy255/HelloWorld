import random

highest = 10
answer = random.randint(1,highest)
print(answer)

print("Please guess a number between 1 and {}".format(highest))
guess = None

while answer != guess:
    guess = int(input())
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