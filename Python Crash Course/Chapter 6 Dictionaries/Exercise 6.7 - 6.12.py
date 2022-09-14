#Exercise 6.7
print("Exercise 6.7")
person = {'name': 'Tiffany Wong', 'race': 'asian',
          'height': '65cm', 'haircolor': 'black', 'age': '35',
          'location': 'kirkland'}
person_2 = {'name': 'brian dy', 'race': 'asian',
            'height': '67cm', 'haircolor': 'black', 'age': '37',
            'location': 'redmond'}
person_3 = {'name': 'jerry douglas', 'race': 'caucasion',
            'height': '50cm', 'haircolor': 'blonde', 'age': '42',
            'location': 'seattle'}

people = [person, person_2, person_3]
for peop in people:
    print(f"Name: {peop['name'].title()} \nRace:{peop['race'].title()}"
          f"\nHeight: {peop['height']} \nHaircolor:{peop['haircolor'].title()}"
          f"\nAge:{peop['age']} \nLocation: {peop['location']} \n")

#Exercise 6.8
print("Exericse 6.8")

pets = []
pet = {'animal type': 'python',
       'name': 'john',
       'owner': 'guido',
       'weight': '43',
       'eats': 'bugs'
}
pets.append(pet)
pet = {'animal type': 'chicken',
       'name': 'clarence',
       'owner': 'tiffany',
       'weight': '2',
       'eats': 'seeds'
       }
pets.append(pet)

pet = {'animal type': 'dog',
       'name': 'peso',
       'owner': 'eric',
       'weight': '37',
       'eats': 'shoes'
       }
pets.append(pet)

for pet in pets:
    print(f"Here's what I know about {pet['name'].title()}")
    for key, value in pet.items():
        print(f"\t{key.title()}: {value.title()}")

#Exercise 6.9
print("Exercise 6.9")
favorite_places = {'eric': ['iceland', 'norway', 'sweeden'],
                   'sam': ['usa', 'alaska'],
                   'derick': ['egypt', 'morocco'],
                   'david': ['london']
                   }

for name,places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places to visit:")

    for place in places:
        if len(places) >1:
            print(f"\t{place.title()}")
        else:
            print(f"is {place.title()}\t")

#Exercise 6.10
print('Exercise 6.10')
favorite_number = {'brian': [7,21,33], 'tiffany': [11,6,31], 'patrick': [19,51,2],
                   'david': [99], 'john': [561,0]}

for name, number in favorite_number.items():
    print(name.title().rstrip(),"'s favorite number is:")
    for numbers in number:
        print(f"\t{numbers}")

#Exercise 6.11
print('Exercise 6.11')
city = {
    'santiago': {
        'country': 'chile',
        'population': '6_310_100',
        'fact': 'andes mountains',
    },
    'talkeetna': {
        'country': 'USA',
        'population': '876',
        'fact': 'alaska range',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': '975_348',
        'fact': 'himalaya'
    }
}

for name, city_info in city.items():
    print(f"\n{name.title()}")
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print(f"\tCountry: {country.title()}"
          f"\tPopulation: {population.title()}"
          f"\tFact: {fact.title()}")

