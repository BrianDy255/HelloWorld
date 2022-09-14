answer = 17

if answer != 42:
    print("That is not the correct anaswer. Please try again")

print("***" * 21)
age_0 = 22
age_1 = 18

#using the AND statement. Both must be correct for it to be true
#adding the print(bool) statement lets me know if the statement is true or false
print(bool(age_0 >= 21 and age_1 >= 21))
print("***" * 21)

age_1 = 22
print(bool((age_0 >= 21) and (age_1 >= 21)))
print("***" * 21)

#using the OR statement. Either statement must be correct to be true
age_0 = 22
age_1 = 18
print(bool(age_0 >= 21 or age_1 >= 21))
print("***" * 21)

age_0 = 18
print(bool(age_0>=21 or age_1 >= 21))
print("***" * 21)

#using the IN statement.
requested_topings = ['mushrooms', 'onions', 'pineapple']
print(bool('mushrooms' in requested_topings))
print(bool('pepperoni' in requested_topings))

