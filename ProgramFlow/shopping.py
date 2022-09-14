shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item == "spam":
#         continue                #the continue allows everything in the loop to be ignored. So in this example, since spam == item, it will continue iterating the list.
#     print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        break                   #the break allows everything in the loop to stop. Helps to "find" something you're looking for if there's a long list.
    print("Buy " + item)