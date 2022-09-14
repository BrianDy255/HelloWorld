count = 1
while count <= 5:
    print(count)
    count +=1

print("++++++" * 20)
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number %2 == 0:
        continue

    print(current_number)