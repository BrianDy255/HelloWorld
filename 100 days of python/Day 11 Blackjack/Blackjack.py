##things to do. Make a function to compare cards. Currently too cluttered. Would be cleaner to add the function to compare.

import art
import random

print(art.logo)
user_cards = []
computer_cards = []

# a function to deal out the cards to the user and the computer
def deal_cards():
    user_cards.append(int(random.choice(cards)))
    user_cards.append(int(random.choice(cards)))
    computer_cards.append(int(random.choice(cards)))
    print(f"Your cards: {user_cards}")
    print(f"Computer shows: {computer_cards}")


# Add up the cards for the user using recursion
def calculate_cards(user_cards):
    if len(user_cards) == 0:
        return 0
    return user_cards[0] + calculate_cards(user_cards[1:])


# used for the user to accept another card if user selects "y"
def deal_another_user_card():
    user_cards.append(int(random.choice(cards)))


# deals the computer their next card.
def deal_computer_card():
    computer_cards.append(random.choice(cards))


cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# create the cards for the user and the computer


def convert_ace():
    if 11 < calculate_cards(user_cards) <= 21:
        cards[0] = 1
    if 11 < calculate_cards(computer_cards) <= 21:
        cards[0] = 1


def is_twenty_one():
    if user_cards == [11, 10] or user_cards == [10, 11]:
        print("You got a Black Jack! You Win")
        exit()
    elif computer_cards == [11, 10] or computer_cards == [10, 11]:
        print(calculate_cards(computer_cards))
        print("Computer has blackjack. You lose")


def draw():
    if user_cards == computer_cards:
        print("It's a Draw.")


def computer_turn():
    deal_computer_card()
    is_twenty_one()
    draw()


def play_game():
    deal_cards()
    # Need to fix so that once you select no, it should not have to ask you again
    while True:
        # Check if the user has a blackjack first. If yes, needs to end the game.
        is_twenty_one()
        print(f'Your Total: {calculate_cards(user_cards)}')
        # Checks to make sure that if the user has < 11 the Ace becomes a one.
        convert_ace()
        ask_for_card = input("Type 'y' to get another card, type 'n' to pass: ")
        calculate_cards(user_cards)
        if ask_for_card == 'y':
            deal_another_user_card()
            calculate_cards(user_cards)
            print(f'\tPlayer Cards: {user_cards}')
            print(f'\tPlayer has {calculate_cards(user_cards)}')
            if calculate_cards(user_cards) > 21:
                print("You Busted!")
                exit()
            if user_cards == [11, 11]:
                user_cards[0] = 1
                print(user_cards)
        elif ask_for_card == 'n':
            # Resets the ace back to 11 for the computer
            cards[0] = 11
            while True:
                if calculate_cards(computer_cards) < 17:
                    computer_turn()
                    is_twenty_one()
                print(f'\tComputer Cards: {computer_cards}')
                convert_ace()
                if 21 >= calculate_cards(computer_cards) > calculate_cards(
                        user_cards):
                    print(
                        f'Computer has: {calculate_cards(computer_cards)} \t Player has: {calculate_cards(user_cards)}. YOU LOSE!')
                    exit()
                if 17 <= calculate_cards(computer_cards) <= 21:
                    if calculate_cards(computer_cards) > calculate_cards(user_cards):
                        print(
                            f'Computer has: {calculate_cards(computer_cards)} \t Player has: {calculate_cards(user_cards)}. YOU LOSE!')
                        exit()
                    elif calculate_cards(computer_cards) > calculate_cards(user_cards):
                        print(f"Computer has: {computer_cards} \nPlayer has:{calculate_cards(user_cards)}")
                        print(f'***** You Win *****')
                        exit()
                    elif calculate_cards(computer_cards) == calculate_cards(user_cards):
                        print(
                            f'Computer has: {calculate_cards(computer_cards)} \t Player has: {calculate_cards(user_cards)}')
                        print("It's a DRAW!")
                        exit()
                    else:
                        print(
                            f'Computer has: {calculate_cards(computer_cards)} \t Player has: {calculate_cards(user_cards)}.')
                        print("**** YOU WIN ****")
                        exit()
                    if calculate_cards(computer_cards) > 22:
                        print(f'Computer Busted! *** You Win ***')
                        print(f"Computer shows: {computer_cards} Computer Total:{calculate_cards(computer_cards)}")
                        exit()
                elif calculate_cards(computer_cards) > 21:
                    print(f"Computer shows: {computer_cards} \tTotal:{calculate_cards(computer_cards)}")
                    print(f'Computer Busted! *** You Win ***')
                    exit()
        else:
            print("Thanks for playing!")


while input("Do you want to play a game of Black Jack? Type 'y' or 'n': ") == 'y':
    play_game()
