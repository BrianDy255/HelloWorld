guest_list = ["Michael", "Calb", "Dennis", "Demetri"]
message = f'Welcome {guest_list}' f', to my house!'

print(message)

print()

message_2 = f'Unfortunately, looks like {guest_list[2]}' f', wont be able to make it!'
print(message_2)
guest_list[2] = "Robert"
print(f'But it looks like {guest_list[2]}' f' will be able to come instead')
print(f'Would like to welcome {guest_list}' f' to this awesome dinner party')
print()
print("Alright looks like we found a bigger dinner table so we can invite more people")

guest_list.insert(0,"Tom")
guest_list.insert(2,"Ricky")
guest_list.append("Royce")
print(f'Would like to welcome {guest_list}' f' to the party!')

print()
print(f'Sorry, everyone. Looks like the dinner table will only fit two people')
revised_guest_list = guest_list.pop()
print(f'Sorry, but I wont be able to invite {revised_guest_list}' f' to the party anymore.')
revised_guest_list = guest_list.pop()
print(f'Sorry, but I wont be able to invite {revised_guest_list}' f' to the party anymore.')
revised_guest_list = guest_list.pop()
print(f'Sorry, but I wont be able to invite {revised_guest_list}' f' to the party anymore.')
revised_guest_list = guest_list.pop()
print(f'Sorry, but I wont be able to invite {revised_guest_list}' f' to the party anymore.')
revised_guest_list = guest_list.pop()
print(f'Sorry, but I wont be able to invite {revised_guest_list}' f' to the party anymore.')
print(guest_list)

print(f'Looks like only {guest_list}' f' will be able to come to the party')

del guest_list[1]
print(guest_list)
del guest_list[0]
print(guest_list)
