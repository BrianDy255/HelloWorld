#dictionary containing a list and another dictionary
states_and_cities_as_dictionary = { #dictionary level 1
    "Washington": { #dictionary level 2
        'popular_cities': ['Seattle', 'Spokane','Tacoma'], #list
        'capital_city': 'Olympia'
    },
    "Oregon" : {
        'popular_cities': ['Portland', 'Bend','Eugene', 'Corvallis'],
        'capital_city': 'Salem'
    },
    "California" : {
        'popular_cities': ['Los Angeles', 'San Francisco','San Diego'],
        'capital_city': 'Sacramento'
    }
}

for popular_cities in states_and_cities_as_dictionary["Washington"]['popular_cities']:
    print(popular_cities)

# #Here's an example of iterating over only the innermost level of a nested collection with only one level of for loop.
# for city in states_and_cities_as_dictionary['Oregon']['popular_cities']:
#     print(city)