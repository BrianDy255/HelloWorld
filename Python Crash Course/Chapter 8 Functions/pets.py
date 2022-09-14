def describe_pet(animal_type,animal_name):
    """Receives input for animal type and animal name for positional argument"""
    print(f'I have a {animal_type}')
    print(f'My {animal_type}"s name is {animal_name.title()}')

#Rewriting to use keyword arguments

def describe_pet(animal_type='dog', animal_name='ben'):
    print(f'I have a {animal_type}. Their name is {animal_name.title()}')

describe_pet()

def describe_pet(animal_name='David',animal_type='Cat'):
    print(f'I have an {animal_type}, and their name is {animal_name.title()}')

describe_pet()

#using Default Values
def describe_pet(animal_name,animal_type = 'dog'):
    print(f'I have a {animal_type}, and its name is {animal_name.title()}')

describe_pet('ben')
describe_pet(animal_name='ben')

jk

