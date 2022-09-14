panagram = "The quick brown fox jumps over the lazy dog"

words = panagram.split()
print(words)



numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

int_num = numbers.split(",")


for index in range(len(int_num)):
    int_num[index] = int(int_num[index])

print(int_num)

integer_values = []
for value in int_num:
    integer_values.append(int(value))

print(integer_values)