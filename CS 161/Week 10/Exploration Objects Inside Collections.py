class Ingredient:

    """
    An Ingredient class for representing an Ingredient object that has name
    """
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

#create various Ingredient objects
puffed_rice = Ingredient("Puffed rice")
cream = Ingredient("Cream")
spinach = Ingredient("Spinach")
brocolli = Ingredient("Brocolli")
potatoes = Ingredient("Potatoes")
tomatoes = Ingredient("Tomatoes")
tamarind_juice = Ingredient("Tamarind juice")
red_chilli_powder = Ingredient("Red chilli powder")
cinnamon = Ingredient("Cinnamon")

ground_coriander = Ingredient("Ground Coriander")
salt = Ingredient("Salt")

#now store Ingredient objects inside a list
list_of_spices = [red_chilli_powder, salt]

#add an object after a list has been already created
list_of_spices.append(ground_coriander)
list_of_spices.append(cinnamon)
list_of_spices.append(salt)

#dictionary of ingredients
raw_ingredients_dictionary = {
    "Potatoes" : potatoes,
    "Tomatoes" : tomatoes,
}

#add an object the dictionary has been already created
raw_ingredients_dictionary["Spinach"] = spinach

print("List of spices", list_of_spices
      )
print() #print a blank line

print("Dictionary of raw ingredients", raw_ingredients_dictionary)

print("Name of this ingredient is", tamarind_juice.get_name())

for spice in list_of_spices:
    print(spice.get_name())