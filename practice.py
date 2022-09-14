import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []

user_cards.append(random.choice(cards))
user_cards.append(random.choice(cards))
print(user_cards)

def add_cards(user_cards):
    print(user_cards)
    if len(user_cards) == 0:
        return 0
    return user_cards[0] + add_cards(user_cards[1:])

print(add_cards(user_cards))