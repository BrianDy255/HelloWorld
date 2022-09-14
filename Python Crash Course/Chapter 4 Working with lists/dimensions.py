#tuples are basically list that are immutable (non-changing)
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
print(dimensions)
print("---" * 10)
# dimensions[0] = 250 # when you try to change the first index at 0, it will produce an error because you can't change the item due to tuple

my_t = 3, #tuple is indicated by a comma. Can also be written as (3,) and it produces the same results
print(my_t)

print("---" * 10)
print("\nOriginal dimensions")
for dimension in dimensions:
    print(dimension)

dimensions = (400,200)
print("\nNew dimensions")
for dimension in dimensions:
    print(dimension)
print("---" * 10)

