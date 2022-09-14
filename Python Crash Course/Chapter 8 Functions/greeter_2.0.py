def get_formatted_name(first_name,last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()

while True:
    print("Please tell me your name: ")
    f_name = input("Input your first name>>> ")
    if f_name == 'quit':
        print("Thanks for playing")
        break
    l_name = input("Now your last name>>>")
    if l_name == 'quit':
        print("Quitting session")
        break

    name = get_formatted_name(f_name,l_name)
    print(f'Greetings, {name}')
