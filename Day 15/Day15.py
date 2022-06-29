#coffee machine
import resource

from sympy import re


MENU = {
    'espresso': {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    'latte': {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    'cappuccino': {
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
    "money" : 0
}

coffee_on = True

def user_prompt():
    coffee = input("What would you like? (espresso/latte/cappuccino):")
    return coffee

def check_if_can_make_coffee(resources, recipe):
    can_make = True
    if "milk" in recipe:
        if recipe["milk"] > resources["milk"]:
            can_make = False    
    if "water" in recipe:
        if recipe["water"] > resources["water"]:
            can_make = False    
    if "coffee" in recipe:
        if recipe["coffee"] > resources["coffee"]:
            can_make = False  
    return can_make

def print_report(resources):
    for res, val in resources.items():
        print(f"{res} : {val}")

def coffee_machine(selected):
    coffee = selected
    can_make = check_if_can_make_coffee(resources, MENU[coffee]["ingredients"])
    if can_make:
        money_entered = 0        
        quarters = int(input("Please enter a number of quarters you enter: "))
        money_entered = money_entered + (quarters * 0.25)
        dimes = int(input("Please enter a number of dimes you enter: "))
        money_entered = money_entered + (dimes * 0.10)
        nickels = int(input("Please enter a number of nickels you enter: "))
        money_entered = money_entered + (nickels * 0.05)
        pennies = int(input("Please enter a number of pennies you enter: "))
        money_entered = money_entered + (pennies * 0.01)

        if(money_entered >= int(MENU[coffee]["cost"])):
            if "milk" in MENU[coffee]["ingredients"]:
                resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
            if "water" in MENU[coffee]["ingredients"]:                
                resources["water"] -= MENU[coffee]["ingredients"]["water"]   
            if "coffee" in MENU[coffee]["ingredients"]:                
                resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
            
            print(f"Here is {money_entered - int(MENU[coffee]['cost'])} dollars in change.")
            money_entered = MENU[coffee]["cost"]
            resources["money"] += money_entered
            print(f"Here is you {coffee}. Enjoy!")
        else:
            print("Sorry, not enough money, refunded.")
    else:
        print("Sorry there are not enough resources in coffee machine")

while coffee_on:
    choice = user_prompt()

    if choice == "report":
        print_report(resources)
    elif choice == "off":
        coffee_on = False
    elif choice.lower() == "cappucino":
        coffee_machine(choice)
    elif choice.lower() == "latte":
        coffee_machine(choice)
    elif choice.lower() == "espresso":
        coffee_machine(choice)
