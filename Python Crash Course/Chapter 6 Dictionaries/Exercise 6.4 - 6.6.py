#Exercise 6.4
print("Exercise 6.4 \n")
glossary = {'range': 'Provides a range of numbers',
            'list()': 'creates a list',
            'lstrip()': 'strips the left indent',
            'rstrip()': 'strips the right indent',
            'len()': 'finds the length of a given string or int',
            'set()': 'Set items are unordered, unchangeable, ' \
                     'and do not allow duplicate values',
            'min()': 'finds the minimum number in a list',
            'max()': 'finds the maximum number in a list',
            'sum()': 'finds the  sum of a number in a list'
            }

for key, values in glossary.items():
    print(f'{key}, {values.title()}')

#Exercise 6.5
print("\nExercise 6.5 \n")

rivers = {'colorado River': 'USA',
          'Yangzi River': 'China',
          'nile river': 'located in Egypt'}

for river, country in rivers.items():
    print(f"The {river.title()} is located in {country}")

print("")
for river in rivers.keys():
    print(f"Rivers: {river.title()}")

print("")
for river in rivers.values():
    print(f"Countries: {river}")

#Exercise 6.6
print("\nExercise 6.6")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'tiffany': 'ruby',
    'phil': 'python',
    'david': 'ruby',
    'phillis': 'c++',
    'dafny': 'ruby on rails',
    'brian': 'kotlin'
}
print("")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite programming language is {language}")
print("")

friends = ['tiffany', 'phil', 'brian']
for name,language in favorite_languages.items():
    if name in friends:
        print(f"{name.title()}, Thanks for already taking the poll!"
              f"You're favorite programming language is "
              f"{language}\n")
    if name not in friends:
        print(f"{name.title()}, please take the time to"
              f" sign up for the poll!\n")

#removing duplicates. Use the set and need to add the values method at the end

for language in set(favorite_languages.values()):
    print(language)
print("")

#sorting the names

for name, language in sorted(favorite_languages.items()):
    print(f"{name.title()}'s favorite programming language is {language}.")
print("")