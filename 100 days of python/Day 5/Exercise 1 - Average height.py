# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total = 0
for sum in student_heights:
    total += sum
print(total)

count = 0
for num in student_heights:
    count +=1

print(round(total/count))





