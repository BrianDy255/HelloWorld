age = int(input("How old are you? "))

# if age >= 16 and age <=65:              # Both conditions have to be true
#     print("Have a good day at work")

## Simplified Chain Comparison ##
if 16 <= age <= 65:
    print("Have a good day at work")            #this code is the same as above, just written a little more simpler
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")

#####################
## Using "in range" loop##
#####################

if age in range(16,66):
    print("*" * 10)
    print("Have a good day at work")