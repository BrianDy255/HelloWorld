visit = ["tokyo", "antarctica", "peru", "norway", "bora bora"]
print(visit)


print(f' \nThis is the sorted list', sorted(visit))
print(f' \nThis is the original list again.', visit)

sorted_reverse = sorted(visit)
sorted_reverse.sort(reverse=True)
print( f' \nThis is the sorted reverse list' ,sorted_reverse)
print(f' \nThis is the original list again.', visit)

visit.reverse()
print(visit)
visit.reverse()
print(visit)

visit.sort()
print(visit)
visit.sort(reverse=True)
print(visit)

guest_list = ["Michael", "Calb", "Dennis", "Demetri"]

print(f' We are inviting ', len(guest_list), f' to the party tonight')