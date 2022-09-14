low = 1
high = 1000

print("Please think of a number between {}, {}".format(low, high))
input("Press Enter to Start")

guesses = 1

while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess was correct)"
                     .format(guess)).casefold()                         #the "reformat code" under the "code" tab can help organize the formatting better for things that have a long string.
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes 1 less than the guess.
        high = guess + 1
    elif high_low == "c":
        print("I got it in {} guesses".format(guesses))
        break
    else:
        print("Please enter h, l, or c")

    guesses = guesses + 1           #can also be written as guesses += 1 which does the same thing. This is preferred. Also known as an Augmented assignment operator
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))