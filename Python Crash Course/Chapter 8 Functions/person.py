def build_person(f_name,l_name):
    """Using dictionaries in a function"""
    full_name = {"First:": f_name, "Last Name:": l_name}
    return full_name

name = build_person('Tiffany', 'wong')
print(name)

#adding another parameter to the dictionary in a function
def build_person(f_name,l_name,age=None):
    """Adding another paraemter such as age in the dictionary in a function"""
    person = {"First Name:": f_name.title(), "Last Name:": l_name.title()}
    if age:
        person['Age:'] = age
    return person

name = build_person("tiffany", 'wOng', age=35)
print(name)