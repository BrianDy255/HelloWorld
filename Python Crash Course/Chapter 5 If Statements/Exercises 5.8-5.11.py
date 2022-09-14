#exercise 5.8
usernames = ['adam', 'steve', 'admin', 'joseph', 'sarah']

for name in usernames:
    if name == 'admin':
        print(f"Welcome {name.title()}, would you like to see the status report?")
    else:
        print(f"Hello {name.title()}, thanks for logging in again!")

#Exercise 5.9
usernames = []
if name:
    for name in usernames:
        print(f"Welcome {name} to the site!")
    else:
        print("We need to find some new users!")

#Exercise 5.10
current_users = ['adam', 'steve', 'admin', 'joseph', 'sarah']
new_users = ['david', 'ADAM', 'sArah', 'ben', 'olaf']

current_users_lower = [user.lower() for user in current_users] #uses list comprehension. Would be good to review this section

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user.title()} is not available. Please enter a new user name")
    else:
        print("That name is available!")

#Exercise 5.11
numbers = list(range(1,10))

for number in numbers:
    if number == '1':
        print(f"{number}st")
    if number == '2':
        print(f"{number}nd")
    if number == '3':
        print(f"{number}rd")
    else:
        print(f"{number}th")