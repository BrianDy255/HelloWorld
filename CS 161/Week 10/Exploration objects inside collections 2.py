class Recipe:
    """
    A Recipe class for representing a Recipe object that has a name and ingredients
    """
    def __init__(self, name):
        self._name = name

        #starting with an empty dictionary of ingredient objects
        self._ingredients = {} #This would look like ingredient_name: ingredient_object

    def add_ingredient(self, ingredient_object):
        print("Adding ingredient", ingredient_object.get_name())
        ingredient_name = ingredient_object.get_name()
        self._ingredients[ingredient_name] = ingredient_object.get_name()

    def remove_ingredient(self, ingredient_name):
        print("Removing ingredient", ingredient_name)
        self._ingredients.pop(ingredient_name)
        print("Current Ingredients:", self._ingredients)

    def print_ingredients(self):
        print("Ingredients for this recipe are:")
        print(self._ingredients)

class Ingredient:

    """
    An Ingredient class for representing an Ingredient object that has name
    """
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

#now let's use the above class using this test code
bhel_recipe = Recipe("Bhel") #create a Recipe object
puffed_rice_ingredient = Ingredient("Puffed rice") #create an Ingredient object
raw_onions_ingredient = Ingredient("Raw onions")
tomatoes_ingredient = Ingredient("Tomatoes")
tamarind_juice_ingredient = Ingredient("Tamarind juice")
red_chilli_powder_ingredient = Ingredient("Red chilli powder")
ground_coriander_ingredient = Ingredient("Ground Coriander")
salt_ingredient = Ingredient("Salt")

bhel_recipe.add_ingredient(puffed_rice_ingredient) #add an ingredient
bhel_recipe.add_ingredient(raw_onions_ingredient)
bhel_recipe.add_ingredient(tomatoes_ingredient)
bhel_recipe.add_ingredient(red_chilli_powder_ingredient)
bhel_recipe.add_ingredient(ground_coriander_ingredient)
bhel_recipe.add_ingredient(salt_ingredient)
bhel_recipe.remove_ingredient("Salt") #remove an ingredient
bhel_recipe.print_ingredients() #print the list of ingredients so far