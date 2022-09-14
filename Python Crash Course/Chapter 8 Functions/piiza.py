#Mixing positional and arbitrary arguments

def make_pizza(size, *toppings):
    """arbitrary arguments must always come last"""
    print(f'Making a size {size} inch pizza with the following topings: ')
    for topping in toppings:
        print(f' - {topping.title()}')
