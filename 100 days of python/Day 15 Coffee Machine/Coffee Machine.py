menu = {
    "Espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 400,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
from logo import logo
import Menu

print(logo)

end_program = True


def is_resource_sufficient(menu_ingredients):
    for ingredient in menu_ingredients:
        if menu_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry, we don't have enough {ingredient} for your drink.")
            return False
        else:
            return True


def get_money():
    """Takes the amount of money the user provides and calculates the total the user has inputted"""
    print("Please Insert Coins.")
    quarters = int(input("How Many Quarters? "))
    dimes = int(input("How Many dimes? "))
    nickels = int(input("How Many Nickles? "))
    pennies = int(input("How Many Pennies? "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return round(total,2)


def is_transaction_succesful(money_received, drink_cost):
    """Return True when the payment is accepted or False if is insufficient"""
    if money_received > drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded")
        return False


def make_coffee(drink_name,order_ingredients):
    """deduct required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. ")



while end_program:
    user_input = input("What would you like? (Espresso/ Latte / Cappuccino): ").title()

    if user_input == "Off":
        end_program = False
        print("System Shut Down...")
        break
    elif user_input == "Report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}mg")
        print(f"Money: ${profit}")
    else:
        drink = menu[user_input]
        if is_resource_sufficient(drink['ingredients']):
            payment = get_money()
            if is_transaction_succesful(payment, drink['cost']):
                make_coffee(user_input, drink['ingredients'])