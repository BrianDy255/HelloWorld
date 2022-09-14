#Functiosn with more than 1 input
def greet_with(name, location):
    print(f'Hello {name}')
    print(f"What's it like living in {location}?")

greet_with("Brian", "Seattle")

#Functions with Keyword Arguments
greet_with(location="Seattle", name="David")
