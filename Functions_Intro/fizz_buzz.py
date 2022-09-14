def fizz_buzz(number: str) ->str:
    """A game that returns 'fizz' if divisible by 3 and
     'buzz' if the number is divisble by 5"""

    if number % 15 == 0:
        return ("Fizz Buzz")
    elif number %5 == 0:
        return ("Buzz")
    elif number %3 == 0:
        return ("Fizz")
    else:
        return str(number)

comp_value = 1

input("Play Fizz Buzz. Press Enter to Start")
print()

next_number = 0
while next_number <99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = correct_answer
    # players_answer = input("Your Go: ")
    if players_answer != correct_answer:
        print("You Lose, the correct anaswer was {}".format(correct_answer))
        break
else:
    print("Well done you reached {}".format(next_number))