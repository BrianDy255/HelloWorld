# #
# #         012345678901234
# parrot = "Norwegian Blue"
#
# # The last digit in the bracket indicates a "step sequence of 2". So this is read as "Start from 0 which is the letter N and goes up to but not including 6 (letter i) and count the characters in steps of 2 until you hit letter i
# print(parrot[0:6:2]) #Nre
# print(parrot[0:6:3]) #Nw
#
# number = "9,223,372,036,854,775,807"
# print(number[1::4]) #This reads as "Start at char 1 which is the comma and go all the way to the end and count every 4 character from the comma, which produces all commas in this case.
#
# number = "9,223;372:036 854,775;807"
# seperators = (number[1::4])
# print(seperators)
#
# values = "".join(char if char not in seperators else " "for char in number).split()
# print([int(val) for val in values])

#######################
number = input("Please enter a series of numbers, using any separators you like: ")
seperators = ("")
for char in number:
    if not char.isnumeric():
        seperators = seperators + char
print(seperators)

values = "".join(char if char not in seperators else " "for char in number).split()
print([sum(int(val) for val in values]))