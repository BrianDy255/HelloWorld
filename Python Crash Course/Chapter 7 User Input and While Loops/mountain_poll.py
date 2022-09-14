responses = {}
polling_active = True

while polling_active:
    name = input("Please enter your name\n")
    response = input("Which mountain would you like to climb one day?\n ")

    responses[name] = response

    repeat = input("Would you like someone else to take the poll? Yes / No \n")
    if repeat == 'no':
        polling_active = False

print("--- Polling Results ---")
for name, response in responses.items():
    print(f"{name} would love to be able to climb {response}")