from Menu import menu
from Menu import resources
from logo import logo

print(logo)

end_program = True
while end_program:
    user_input = input("What would you like? (Espresso/ Latte / Cappuccino): ")


    def get_money():
        """Takes the amount of money the user provides and calculates the total the user has inputted"""
        print("Please Insert Coins.")
        quarters = int(input("How Many Quarters? "))
        dimes = int(input("How Many dimes? "))
        nickels = int(input("How Many Nickles? "))
        pennies = int(input("How Many Pennies? "))
        total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        return float("{:.3f}".format(total))


    def get_coffee_price():
        if user_input == "espresso":
            coffee = "Espresso"
        elif user_input == "latte":
            coffee = 'Latte'
        else:
            coffee = 'Cappuccino'
        cost = menu[coffee]['cost']
        return float(cost)


    # Used to get the name of the menu drink
    def get_menu_name():
        if user_input == "espresso":
            coffee = "Espresso"
            return coffee
        elif user_input == "latte":
            coffee = 'Latte'
            return coffee
        else:
            coffee = 'Cappuccino'
            return coffee


    # Returns the sale of the price and provides the change for the user
    def total_price(get_money, get_coffee_price):
        return float("{:.3f}".format(get_money - get_coffee_price))


    # returns the amount of water required to make the coffee drink
    def get_water_resources():
        if user_input == "espresso":
            water_resource = menu["Espresso"]['ingredients']['water']
            return water_resource
        elif user_input == "latte":
            water_resource = menu["Latte"]['ingredients']['water']
            return water_resource
        else:
            water_resource = menu["Cappuccino"]['ingredients']['water']
            return water_resource


    # returns the amount of coffee beans required in the coffee drink
    def get_coffee_resource():
        if user_input == "espresso":
            coffee_resource = menu["Espresso"]['ingredients']['coffee']
            return coffee_resource
        elif user_input == "latte":
            coffee_resource = menu["Latte"]['ingredients']['coffee']
            return coffee_resource
        else:
            coffee_resource = menu["Cappuccino"]['ingredients']['coffee']
            return coffee_resource


    def get_milk_resource():
        if user_input == "latte":
            milk_resource = menu["Latte"]['ingredients']['milk']
            return milk_resource
        elif user_input == "cappuccino":
            milk_resource = menu["Cappuccino"]['ingredients']['milk']
            return milk_resource

        # Updates the resource for water after a user purchases a coffee drink from the machine
    def update_water_resources():
        x = resources['Water'] - get_water_resources()
        resources['Water'] = x
        return resources['Water']

    # Updates the resource for coffee after a user purchases a coffee drink from the machine
    def update_coffee_resource():
        x = resources['Coffee'] - get_coffee_resource()
        resources['Coffee'] = x
        return resources['Coffee']

    def update_milk_resource():
        x = resources['Milk'] - get_milk_resource()
        resources['Milk'] = x
        return resources['Milk']

    def add_money_resources():
        """Adds the money that was used to buy the drink to the resources pool for the machine"""
        if user_input == "espresso":
            add_cost = menu['Espresso']['cost']
            money = resources['Money'] + add_cost
            resources['Money'] = money
            return resources['Money']
        elif user_input == 'latte':
            add_cost = menu['Latte']['cost']
            money = resources['Money'] + add_cost
            resources['Money'] = money
            return resources['Money']
        elif user_input == 'cappuccino':
            add_cost = menu['Cappuccino']['cost']
            money = resources['Money'] + add_cost
            resources['Money'] = money
            return resources['Money']


    def check_ingredients(resources):
        """Checks the resources of the machine vs what the user has ordered. If there is not enough
        of an ingredient, it will let the user know and will not produce a product"""
        #check for water ingredient
        if user_input == 'espresso':
            if resources['Water'] <= get_water_resources():
                print('Sorry there is not enough water.')
                exit()
            elif resources['Coffee'] <= get_coffee_resource():
                print('Sorry there is not enough coffee beans.')
                exit()
        elif user_input == 'latte':
            if resources['Water'] <= get_water_resources():
                print('Sorry there is not enough water.')
                exit()
            elif resources['Coffee'] <= get_coffee_resource():
                print('Sorry there is not enough coffee beans.')
                exit()
            elif resources['Milk'] <= get_milk_resource():
                print('Sorry there is not enough milk.')
                exit()
        elif user_input == 'cappuccino':
            if resources['Water'] <= get_water_resources():
                print('Sorry there is not enough water.')
                exit()
            elif resources['Coffee'] <= get_coffee_resource():
                print('Sorry there is not enough coffee beans.')
                exit()
            elif resources['Milk'] <= get_milk_resource():
                print('Sorry there is not enough milk.')
                exit()

    #check the ingredients after every cycle to determine if there are enough to order another drink
    check_ingredients(resources)
    name_of_coffee = get_menu_name()

    if user_input == "report":
        for keys, values in resources.items():
            print(keys, values)
    elif user_input == "espresso".lower():
        update_coffee_resource()
        update_water_resources()
        add_money_resources()
        print(f"Here is ${total_price(get_money(), get_coffee_price())} in change.")
        print(f"Here's your {name_of_coffee}")
    elif user_input == 'latte'.lower():
        update_coffee_resource()
        update_water_resources()
        update_milk_resource()
        add_money_resources()
        print(f"Here is ${total_price(get_money(), get_coffee_price())} in change.")
        print(f"Here's your {name_of_coffee}")
    else:
        update_coffee_resource()
        update_water_resources()
        update_milk_resource()
        add_money_resources()
        print(f"Here is ${total_price(get_money(), get_coffee_price())} in change.")
        print(f"Here's your {name_of_coffee} ☕")
