#Exercise 7.1
print("Exercise 7.1")

rental_car = input("What kind of car are you looking to rent? \n>>")
print(f"Let me see if I can find the {rental_car} you're looking for")

#Exercise 7.2
print("Exercise 7.2")

seating = input("How many people are in your party?")
seating = int(seating)

if seating > 8:
    print("You'll have to wait a few minutes before being seated")
else:
    print("Follow your waitress to the table")

#Exercise 7.3
print("Exercise 7.3")

num = input("Please enter a number: ")
num = int(num)

if num % 10 == 0:
    print(f"{num} is divisible by 10")
else:
    print(f"{num} is not divisible by 10")