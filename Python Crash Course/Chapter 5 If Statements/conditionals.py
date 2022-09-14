age = 37
if age >= 40 or age >= 37:
    print("You're not that old yet!")
print("***" * 21,"\n")

#testing normal case
name = 'brian '
if name == 'Brian':
    print(f'Hello {name}')
else:
    print("What is your name?")
print("***" * 21,"\n")

#using the .lower to make it not case sensitive
name = 'Brian'
if name.lower().lstrip() == 'brian':
    print(f'Hello {name.title()}')
else:
    print("What is your name?")

fruit = ['apple', 'oranges', 'banana']
print("***" * 21,"\n")

#using the IN statement
if 'tomato' in fruit:
    print("Does not have this fruit in here")
else:
    print("Need to buy more")
print("***" * 21,"\n")

#using the NOT IN statement
if 'tomato' not in fruit:
    print("You are fine with the ingredients")
else:
    print("Need to buy more")