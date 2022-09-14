import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_0 = 0
paper_1 = 1
scissors_2 = 2

game_images = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
computer_input = random.randint(0,2)
if user_input >=3 or user_input < 0:
    print("You chose a invalid number. You Lose")
else:
    print(f'{game_images[user_input]}')
    print("Computer chose:")
    print(f'{game_images[computer_input]}')

if user_input == computer_input:
    print("DRAW")
elif user_input == rock_0:
    if computer_input == scissors_2:
        print("You WIN! Rock Beats Scissors")
    else:
        print("You lose!")
elif user_input == paper_1:
    if computer_input == rock_0:
        print("You Win! Paper beats Rock")
    else:
        print("You Lose! Scissors beats Paper")
elif user_input == scissors_2:
    if computer_input == paper_1:
        print("You Win!. Scissors Beats Paper")
    else:
        print("You Lose! Rock Beats Scissors")





