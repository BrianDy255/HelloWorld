cars = ['bmw', 'audi', 'toyota', 'mercedes ']
print("Here is the Original List")
print(cars)

print("\nNow here is the updated sorted list")
sorted_cars_list = sorted(cars)
sorted_cars_list.sort(reverse=True)
print(sorted_cars_list)

cars.reverse()
print(cars)

print(len(cars))