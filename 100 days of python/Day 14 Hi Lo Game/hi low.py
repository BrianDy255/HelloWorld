import art

print(art.logo)
import game_data
import random

# take the first random person from the list to compare against the next person on the list
# if followers that the user chooses is higher, then that comparison becomes "b" and the next person on the list becomes "A"


# Create a variable that keeps track of the score or "count" of how many times the user gets correct.

# Randomize the first comparison and assign it a new variable
compare_a = random.choice(game_data.data)

# randomize the second comparison and assign to another variable
compare_b = random.choice(game_data.data)

def get_random_account():
    return random.choice(game_data.data)


def format_name(compare_a, compare_b):
    """A function to format the structure to produce the "name" compared, "the job title, and "location" """
    print (f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
    print(art.vs)
    print (f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")


# However, must make sure that the comparison variables != the same value to compare to.
score = 0

# lets gets a function that can get the index and appropriate followers to compare to.
#
def hi_low(compare_a, compare_b, score):
    while True:
        #Randomizes "B" after chosing the right answer
        compare_b = random.choice(game_data.data)
        #If A happens to == B, get another random choice for B
        if compare_a == compare_b:
            compare_b = random.choice(game_data.data)
        format_name(compare_a, compare_b)
        follower1 = compare_a['follower_count']
        follower2 = compare_b['follower_count']
        user_input = input("Who has more followers? Type 'A' or 'B'")
        if user_input == "A".lower():
            if follower1 > follower2:
                score += 1
                print(f"You're right! Current Score: {score}")
                compare_a = compare_b
            else:
                print(f"Sorry, that's wrong. Final Score: {score}")
                play_again()
        elif user_input == "b".lower():
            if follower1 < follower2:
                score += 1
                print(f"You're right! Current Score: {score}")
                compare_a = compare_b
            else:
                print(f"Sorry, that's wrong. Final Score: {score}")
                play_again()
                exit()

def play_again():
    user = input("Would you like to play again? Type 'y or 'n'").lower()
    if user == 'y':
        hi_low(compare_a,compare_b,score)
    else:
        exit()


hi_low(compare_a, compare_b, score)