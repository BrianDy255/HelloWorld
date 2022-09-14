letters = "abcdefghijklmnopqrstuvwxyz"
#Remember, not including a start or stop value will allow you to include everything in the string. Remember, the digits goes UP TO but does not INCLUDE the value. So if you were to put a 0, the "a" would not show up cause it goes up to but does not include the "a" value

backwards = letters[::-1]
print(backwards)

#using the [::-1] is common in python. It is considered a negative step. REVERSES A SEQUENCE

#Challenge
# 1)Create a slice that produces the characters qpo
# 2)Slice the string to produce edcba
# 3)slice the string to produce the last 8 characters, in reverse order.

#1
print(letters[16:13:-1])

#2
print(letters[4::-1])

#3
print(letters[25:17:-1])
#or can also do this way
print(letters[:-9:-1])

print(letters[-4:])
print(letters[-1:])
print(letters[:1])