requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print("hold the anchovies!".title())
print("***" * 21,"\n")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print(f'Finished making your pizza!')

print("***" * 21,"\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f'Adding {requested_topping} to the pizza!')

print("***" * 21,"\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we're out of green peppers!")
    else:
        print(f'Adding {requested_topping} to the pizza!')

print("***" * 21,"\n")

requested_toppings = []
if requested_toppings: #since the list is empty, it bypasses this if statement and goes straight to the else clause
    for requested_topping in requested_toppings:
        print("Adding {} to the pizza".format(requested_topping))
else:
    print("Are you sure you want a plain pizza?")

print("***" * 21,"\n")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding {} to your pizza!".format(requested_topping))
    else:
        print(f'Sorry, we dont have {requested_topping}')