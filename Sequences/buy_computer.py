available_parts = ["Computer,",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "HDMI Cable",
                   "DVD Drive"
                   ]
# valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
# print(valid_choices)
current_choice = "-"
computer_parts = [] #creates an empty list.

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_parts = available_parts[index]
        if chosen_parts in computer_parts:
            print("Removing {}".format(computer_parts))
            computer_parts.remove(chosen_parts)
        else:
            print("Adding {}".format(chosen_parts))
            computer_parts.append(chosen_parts)
        print("Added {}" .format(computer_parts), " to the list" )

    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
           print("{0}: {1}".format(number+1, part))

    current_choice = input()
    print(type(current_choice))

print(computer_parts)