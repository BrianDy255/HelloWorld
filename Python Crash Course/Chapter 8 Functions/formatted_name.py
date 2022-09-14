def get_formatted_name(f_name,l_name):
    """Neatly outputs a full and last name"""
    full_name = f'{f_name} {l_name}'
    return full_name.title()

name = get_formatted_name('leslie', 'james')
print(name)

#making an optional argument
def get_formatted_name(f_name,l_name,middle_name =""):
    """Adding an optional argument. Add the empty string"""
    if middle_name:
        full_name = f'{f_name} {middle_name} {l_name}'
    else:
        full_name = f'{f_name} {l_name}'
    return full_name.title()

name = get_formatted_name('Tiffany','lee','wong')
print(name)

name = get_formatted_name('tiffany', 'wong')
print(name)

