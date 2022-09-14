age = 24
print("My age is " + str(age) + " years") #using the str function forces the item / variable to become a string
print("My age is {0} years".format(age))


#These are replaced with the values in the parentheses after .format.
#The first value goes into {0}, the second into {1}, and so on.

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "July", "Aug", "Oct", "Dec"))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}"
      .format(28,30,31))
