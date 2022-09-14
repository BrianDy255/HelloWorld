#exercise 5.3
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

#exercise 5.4
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'red':
    print("You just earned 10 points!!")

#exercise 5.4 version 2
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!!")

#Exercise 5.5
alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!!")
elif alien_color == 'red':
    print("You earned 15 points!")

#Can also be rewritten as:
alien_color = 'red'
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15

print(f'You earned {points} points!')

print("***" * 21,"\n")

#Exercise 5.6
age = 16
message = ""
if age < 2:
    message = "This is a baby"
elif 2 <= age < 4:
    message = "This is a toddler"
elif 4 <= age < 13:
    message = "This is a kid"
elif 13 <= age < 20:
    message = "This is a teenager"
elif 20 <= age < 65:
    message = 'This is an adult'
elif age >= 65:
    message = 'Thi sis an elder person'

print(message)

#exercise 5.7
favorite_fruit = ['mango', 'watermelon', 'blueberries', 'papaya',
                  'banana','lychee', 'cherry']

if 'mango' in favorite_fruit:
    print('You really like {}'.format(favorite_fruit[0]))
if 'banana' in favorite_fruit:
    print(f'You really like {favorite_fruit[4]}!')
if 'tangerines' in favorite_fruit:
    print("You really like tangerines!")
