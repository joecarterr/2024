import os
import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

again = True

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}


def clear_screen():
    os.system("cls")

def process_coins(coffee_type):
    total = 0
    change = 0
    cost = MENU[coffee_type]["cost"]
    pennies = int(input("How many pennies do you have?: "))
    nickels = int(input("How many nickels do you have?: "))
    dimes = int(input("How many dimes do you have?: "))
    quarter = int(input("How many quarters do you have?: "))
    total = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.10) + (quarter * 0.25)
    change = total - cost

    if total >= cost:
        print(f"You have £{total} and a {coffee_type} costs £{cost}...\nPayment accepted, you have £{change} in change.")
        resources["money"] += cost
        resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
        time.sleep(5)
        clear_screen()
    else:
        print(f"Sorry, you have insufficient funds to produce a {coffee_type}...\nYou had £{total} but £{cost} was needed for a {coffee_type}\n You have been refunded {cost} for this coffee")
        time.sleep(5)
        clear_screen()

def create_coffee(coffee_type):
    if resources["water"] > MENU[coffee_type]["ingredients"]["water"]:
        if resources["milk"] > MENU[coffee_type]["ingredients"]["milk"]:
            if resources["coffee"] > MENU[coffee_type]["ingredients"]["coffee"]:
                print("Sufficient ingredients")
                time.sleep(.1)
                process_coins(coffee_type)
    else:
        print("Sorry there were insufficient ingredients to produce your coffee.")


while again:
    coffee = input("What coffee would you like? (espresso, latte or cappuccino): ").lower()

    if coffee == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: £{resources['money']}.")
    if coffee == "off":
        again = False
    if coffee == "latte" or coffee == "espresso" or coffee == "cappuccino":
        create_coffee(coffee_type=coffee)

# TODO: 1