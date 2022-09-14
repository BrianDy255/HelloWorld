# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#
# item_to_find = "spam"
# found_at = None
#
# for index in range(len(shopping_list)):             #len is short for "length". Helps to find the number in a sequence. The equivalent for writing this can also be "for index in range(6)"
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
# print("Item found at position {}".format(found_at))


############################################

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

# for index in range(len(shopping_list)):             #len is short for "length". Helps to find the number in a sequence. The equivalent for writing this can also be "for index in range(6)"
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
    print("Item found at position {}".format(found_at))

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} is not found".format(item_to_find))