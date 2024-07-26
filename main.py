MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1. Asking user for his choice of coffee.

profit = 0
machine_on = True


def user_money_calculation():
    """return amt of money user provided."""
    print("Please insert coins.")
    total = int(input("how many quarters? "))* 0.25
    total += int(input("how many dimes? "))* 0.1
    total += int(input("how many nickels? "))* 0.5
    total += int(input("how many pennies? "))* 0.01
    return total


def money_sufficient(user_money, cost_of_baverage):
    """checks if user provided with enough money."""
    if user_money >= cost_of_baverage:
        global profit
        profit += user_money
        change = round(user_money - cost_of_baverage, 2)
        print(f"Here's your coffee and your change of ${change}.")
        return True
    else:
        print("Sorry the amount money you provided is not sufficient. Money refunded.")
        return False


def resource_sufficient(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"sorry, not enough {items}.")
            return False
    return True

def resource_amt_deduction(baverage, ingredients):
    for items in ingredients:
        resources[items] -= ingredients[items]
    print(f"here is your {baverage}. Thankyou!")

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        machine_on = False
    if user_choice == "report":
        print(f"water: {resources['water']}ml\nmilk: {resources['milk']}ml\ncoffee: {resources['coffee']}g")
        print(f"cost: ${profit}")
    else:
        baverage = MENU[user_choice]
        if resource_sufficient(baverage["ingredients"]):
            user_money = user_money_calculation()
            cost_of_baverage = baverage["cost"]
            if money_sufficient(user_money, cost_of_baverage ):
                resource_amt_deduction(user_choice, baverage["ingredients"])








