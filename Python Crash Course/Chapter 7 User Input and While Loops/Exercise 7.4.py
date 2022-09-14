#Exercise 7.4
print("Exercise 7.4")

prompt = 'Enter toppings for your pizza'
prompt += '\nEnter "quit" to exit\n'

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"Adding {topping} to your pizza")
    else:
        break