#Use a conditional test in the while statement to stop the loop

# prompt = 'Enter toppings for your pizza'
# prompt += '\nEnter "quit" to exit\n'
#
# while True:
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"Adding {topping} to your pizza!")
#     else:
#         print("Done making the pizza")
#         break

#Use an active variable to control how long the loop runs

prompt = 'Enter toppings for your pizza'
prompt += '\nEnter "quit" to exit\n'

active = True
while active:
    topping = input(prompt)
    if topping != 'quit':
        print(f"Adding {topping} to your pizza!")
    else:
        print("Done making the pizza")
        active = False