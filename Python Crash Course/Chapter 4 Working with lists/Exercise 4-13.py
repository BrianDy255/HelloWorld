basic_foods = ("apple", 'banana',
               'cherry', 'dates', 'figs')
print(type(basic_foods))

for food in basic_foods:
    print(food.title())

# basic_foods[2] = "watermelon"

basic_foods = ("apple", 'watermelon', 'strawberries',
               'dates', 'blackberries')
print(f'\nThe new items on the menu list are \n')
for food in basic_foods:
    print(food.title())

