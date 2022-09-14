prompt = "Enter your age"
prompt += "\nPress 'quit' to exit"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print('\nYour tickets are free')
    elif age < 13:
        print('\nYour tickets are $10')
    else:
        print("\nYour tickets are $15")