print("Exercise 8.12")
def make_sandwiches(size,*toppings):
    print(f'Currently making a {size} sandwich with'
          f' the following toppings: ')
    for topping in toppings:
        print(f' - {topping}')

make_sandwiches('large', 'turkey', 'bacon', 'chedder cheese')
make_sandwiches('12 inch', 'raddish', 'mushrooms', 'lettuce')

print("\nExercise 8.13")

def make_profile(first,last,**user_profile):
    user_profile["First Name: "] = first
    user_profile["Last Name: "] = last
    return user_profile

user_info = make_profile('brian', 'dy',
                         height='5ft 6in',
                         ethnicity = "Asian",
                         Location= 'Philippines')
print(user_info)

print(f'\nExercise 8.14')
def make_car(manufacturer, model, **options):
    car_profile = {
        'Manufacturer': manufacturer.title(),
        'Model': model.title()
    }
    for name, values in options.items():
        car_profile[name] = values
    return car_profile

my_car = make_car('honda', 'accord', color = "blue", rim_size = 18,
                  year=1993)
print(my_car)