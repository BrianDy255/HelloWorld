#Exercise 6.1
print("Exercise 6.1")
person = {'first_name': 'Tiffany',  'last_name': 'wong' , 'race': 'asian',
          'height': '65cm', 'haircolor': 'black', 'age': '35',
          'location': 'kirkland'}

print(person['first_name'])
print(person['last_name'].title())
print(f"Age:", person['age'].title())
print(f"Location:", person['location'].title())

#using a forloop
for i, value in person.items():
    print(i, ":", value)

print("\n")

#Exercise 6.2
print("Exercise 6.2")
favorite_number = {'brian': 7, 'tiffany': 31, 'patrick': 19,
                   'david': 99, 'john': 561}

for name, number in favorite_number.items():
    print(name.title().rstrip(),"'s favorite number is:", number)

print("\n")
#Exercise 6.3
print('Exercise 6.3')

glossary = {'range': 'Provides a range of numbers',
            'list()': 'creates a list',
            'lstrip()': 'strips the left indent',
            'rstrip()': 'strips the right indent',
            'len()': 'finds the length of a given string or int'
            }

for word, definition in glossary.items():
    print(word.title(), ":", definition.title())