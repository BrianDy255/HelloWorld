magicians = ["alice", 'bob', 'terry']
for magician in magicians:
    print(magician.title(), f'performed an awesome magaic trick!')
    print(f"We're looking forward to", magician.title(), f'coming back for the next show\n')
print("---" * 13)
#range
list_num = list(range(7))
print(list_num)
list_num.append(int(8))
print(list_num)
print("---" * 13)
squares = ""
for value in range(1,11):
    squares = (value**2)
    print("The square of {0} is {1}".format(value,squares) )

print("---" * 13)
numbers = [1,2,3,4,5,6,7,8,9,0]
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print("---" * 13)

#list comprehensions
squares = [value **2 for value in range(1,11)]
print(squares)

#slice
players = ['charles', 'david', 'sean', 'akop', 'hosep']
print(players[-3:])

print("For the first three players on the team")
for player in players[:3]:
    print(player.title())

#Copying a List
my_food = ['pizza', 'ice cream', 'donuts', 'french fries']
friends_list = my_food[:] #by adding the [:] it creates and separates the list into its own thing.
print("My favorite food's are, \n ",my_food)
print("My friend's favorite foods are\n",friends_list)

my_food.append('boba')
friends_list.append('cacao')

print(my_food)
print(friends_list)