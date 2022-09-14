#https://app.codingrooms.com/management/assignments/364931/overview
#You are going to write a program that will mark a spot with anX
#In the starting code, you will find a variable called map.
#This map contains a nested list. When map is printed this is what the nested list looks like:
#[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
#This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line.
#['⬜️', '⬜️', '⬜️']
#['⬜️', '⬜️', '⬜️']
#['⬜️', '⬜️', '⬜️']
#Now it looks a bit more like the coordinates of a real map:
#
#
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️"," ️⬜️"]
row2 = ["⬜️","️⬜️"," ️⬜️"]
row3 = ["⬜️","️⬜️"," ️⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#horizontal position gets the index of the 1st digit and can be used to find the column.
horizontal_position = position[0]
#vertical position gets the index of the 2nd digit and can be used to find the row
vertical_position = position[1]

#gets the index of the row item in the list of the map first, followed by the item in the list in the row.
map[int(vertical_position)-1][int(horizontal_position)-1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
