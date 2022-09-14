activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():         #the .casefold() puts the string to lowercase or rather, does not care about case matching
    print("But i want to go to the cinema!")
else:
    print("We're gonna wtch a movie! ")