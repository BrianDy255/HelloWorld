list_friends = ["Patrick", "John", "Henry"]
print(list_friends[2],list_friends[0])

message = f'some of the friends i grew up with was {list_friends[0]}' f' and {list_friends[1]}'
print(message.title())


motorcycles_list = ["Honda", "CBR", "yamaha", "suzuki"]
new_message = f'I used to have a {motorcycles_list[2]}' f' but i ended up selling it because i decided to buy a {motorcycles_list[0]}' f'instead.'
print(new_message.title())

motorcycles_list[0] = "Ducati"
print(motorcycles_list)


#appending an item to a list
motorcycles_list.append("honda")
print(motorcycles_list)


#inserting an item from a list
motorcycles_list.insert(2,"Harley")
print(motorcycles_list)

#deleting an item from a list
del motorcycles_list[2]
print(motorcycles_list)

#popping an item from a list. The pop method takes or "pops out" the last item from a list
popped_motorcycle = motorcycles_list.pop()

print(f'The last motorcycle I had before I decided to not ride anymore was the {popped_motorcycle}')

#popping an item from a specific location
print(motorcycles_list)
popped_motorcycle = motorcycles_list.pop(2)
print(popped_motorcycle)

#removing an item from a list
motorcycles_list.remove('Ducati')
print(motorcycles_list)
print(motorcycles_list.append('ducati'))
print(motorcycles_list)

too_expensive = "ducati"
print(f'I wanted to buy the {too_expensive}' f' but it was just too expensive')
motorcycles_list.remove(too_expensive)
print(motorcycles_list)
