age = 4

if age < 4:
    print("You get in for free!")
elif age < 18:
    print("Your price is $25")
else:
    print("The price is $40")

print("***" * 21,"\n")

#another way to write this can be
age = 54

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 20
else:
    price = 40

print(f'The price of the ticket will be ${price}') #uses the f' format
print("the price of the ticket will be ${}".format(price)) #just practicing using the .format

print("***" * 21,"\n")

print("***" * 21,"\n")

age = 67

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f'The price of the ticket will be ${price}') #uses the f' format
print("the price of the ticket will be ${}".format(price)) #just practicing using the .format
