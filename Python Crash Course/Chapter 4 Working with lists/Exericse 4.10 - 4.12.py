#exercise 4-10
list = ['mouse', 'keyboard', 'monitor', 'processor', 'ram', 'mousepad', 'videocard']
print("The first three items on the list are \n", list[0:3])
print("\nThe three items from the middle of the list are \n", list[2:5])
print("\nThe last three items on the last are \n", list[-3:])

#exercise 4-11
my_pizza = ['pepperoni', 'supreme', 'sausage', 'hawaiian']
your_pizza = my_pizza[:]

my_pizza.append('italian')
your_pizza.append('thai')
print(my_pizza)
print(your_pizza)

#exercise 4-12
for pizza in my_pizza:
    print(pizza)

for pizza in your_pizza:
    print(f'\t', pizza)