print('Exercise 8.3')
def make_shirt(size,message):
    """Takes the size and message to display on a shirt"""
    print(f'The size of this shirt is {size}. The message '
          f'you will be displaying says {message}')

make_shirt('small', 'I was here')


print('\nExercise 8.4')

def make_shirt(message, size='large'):
    print(f'The size of the shirt shows {size}. The message '
          f'that will be printed will be {message}')

make_shirt('Cetaphil')
make_shirt(size='medium', message='Lucerin')

print('\nExercise 8.5')
def describe_city(city_name,country):
    """Allows input of name of city and country"""
    print(f'The city of {city_name.title()} is located in {country.title()}')

describe_city('los angeles','USA')
describe_city(city_name='chicago', country='usa')

def describe_city(city_name,country='Chile'):
    print(f'{city_name.title()}, is located in {country}')

describe_city('santiago')