#
#         012345678901234
parrot = "Norwegian Blue"

#SLICING. The first number or space in the bracket is the start character. The last number or space in the bracket goes up to the character but does not include the character within the range
print(parrot[0:6]) # Norweg. Last character you specificy IS NOT INCLUDED in the slice.  So the 6 index in this case is the "i" but is not included
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9]) # Do not necessarily have to add the "start" value. Interpreted still as "0"

print(parrot[10:14])
print(parrot[10:]) # Do not necessarily have to add the "end" value

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

letters = "abcdefghijklmnopqrstuvwxyz"

print(letters[3:7])