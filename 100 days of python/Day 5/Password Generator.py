#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? Enter 1 - 51\n"))
nr_symbols = int(input(f"How many symbols would you like? Enter 0 - 9\n"))
nr_numbers = int(input(f"How many numbers would you like? Enter 0 - 8\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
# random_letters_index = random.randrange(0,nr_letters)
random_letters = random.shuffle(letters)

#Shuffles the alpha characters and creates a password based off input of how many characters a user wants.
for i in range(0,nr_letters+1):
    random_index_letter = random.randint(0,nr_letters)
    for letter in letters[random_index_letter]:
        password+= letter

#Shuffles the symbols list and adds on to the passwords based off user input
random_symbols = random.shuffle(symbols)
for i in range(0,nr_symbols+1):
    random_index_symbol = random.randint(0,nr_symbols)
    for symbol in symbols[random_index_symbol]:
        password += symbol

random_numbers = random.shuffle(numbers)
for i in range(0,nr_numbers+1):
    random_index_number = random.randint(0,nr_numbers)
    for number in numbers[random_index_number]:
        password += number

#Creates a random password of letters, symbols, and numbers in this order.
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Another version of shuffling the order of letters and symbols using the list() method and joining the passwords.
shuffled_password1 = list(password)
random.shuffle(shuffled_password1)
print("Hard Password version 1:")
print("".join(shuffled_password1))

#in order to create randomization, split the string first, which produces a list and then shuffles it using the random.sample followed by joining the result again.
shuffled_password = "".join(random.sample(password,len(password)))
print("Hard Password version 2:")
print(shuffled_password)
