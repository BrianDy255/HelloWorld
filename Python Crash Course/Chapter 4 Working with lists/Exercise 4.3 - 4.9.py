#Exercise 4.3
count_to_twenty = [i for i in range (1,21)] #trying to use list comprehension to make code shorter
print(count_to_twenty)

for num in range(1,21):
    print(num)
print("---" * 13)
#exercise 4.4
# million = []
# for mil in range (1,1000000):
#     million.append(mil)
#     print(million)
#disabling this code due to output

#exercise 4.5
millon_count = list(range(1,100_00_001)) #the underscore can be used to help with visuals. Similar to "commas" to separate the numbers
print(f'The minimum is', min(millon_count))
print(f'The maximum is', max(millon_count))
print(f'The sum of 1 and 1000000 is', sum(millon_count))
print("---" * 13)
#Exercise 4.6
odd_numbers = list(range(1,20,2))
for num in odd_numbers:
    print(odd_numbers)
print("---" * 13)
#Exercise 4.7
threes = list(range(3,31,3))
for num in threes:
    print(num)
print("---" * 13)
#Exercise 4.8
cubed = []
for num in range(1,11):
    cubes = num ** 3
    cubed.append(cubes)

for cubes in cubed:
    print(cubes)
print("---" * 13)
#Exercise 4.9
cube_comprehension = [cube ** 3 for cube in range(1,11)]
print(cube_comprehension)

for cube in cube_comprehension:
    print(cube)

print("---" * 13)
