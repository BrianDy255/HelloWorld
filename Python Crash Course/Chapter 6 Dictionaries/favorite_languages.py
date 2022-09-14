favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

for name, language in favorite_languages.items():
    print(f"{name.title()} favorite programming language is, {language.title()}")


#Looking through all the keys in a dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in favorite_languages:
    print(name.title())

print("")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    if name in friends:
        language = favorite_languages[name].title()
        print(f"hi {name.title()}, looks like you enjoy {language}")

print("")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("")

#sorting through a dictionary

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking our poll!")

print("")

#Looping through all values in a dictionary
print("The following languages have been mentioned:")
for language in sorted(favorite_languages.values()): #added the sorted just for fun / practice
    print(language.title())

print("")

#Looping through withotu repeating / duplicating the same value using the set()
for language in set(favorite_languages.values()):
    print(language.title())
print("")
print("----" * 10)
#nesting a list in a dictionary
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['C'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    'sam':  ['windows', 'apple', 'linux']
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is {language.title()}")