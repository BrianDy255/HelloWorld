answer = 5

print("Please Guess a number between 1 and 10: ")
guess = int(input())

# if guess < answer:
#     print(" Please guess higher")
# elif guess > answer:
#     print(" Please guess lower")
# else:
#     print("CORRECT!")

##########################
#adding a second guess#

# answer = 5
#
# print("Please Guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess < answer:
#     print(" Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("You are correct!")
#     else:
#         print("Sorry incorrect")
# elif guess > answer:
#     print(" Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("You are correct!")
#     else:
#         print("Sorry that is incorrect")
# else:
#     print("CORRECT!")

###########################
## Conditional Operators - Using the not equal to###
###########################
if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("You got it correct!")
    else:
        print("You are not correct")
else:
    print("You're correct!")

#################
##Challenge######
#################
#Change condition so that
#if guess == answer:
#then change the program to give the correct results

if guess == answer:
    print("You're right the first time!")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("You got it correct!")
    else:
        print("You are not correct")