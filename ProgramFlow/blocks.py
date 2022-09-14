name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name))) #adding the int changes the string to an integer. However, if you put a number that's not an integer it will give an error.
print(age)

if age >= 18:
    print("You're old enough to vote!")
else:
    print("Come back in {0} years".format(18-age))
if age < 18:
    print("Come back in {0} years".format(18-age))
elif age == 900:
    print("youre super old!")
else:
    print("You're old enough to vote!")