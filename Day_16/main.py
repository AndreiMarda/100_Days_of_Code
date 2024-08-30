from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_on = True
Menu_obj = Menu()
CoffeeMaker_obj = CoffeeMaker()
MoneyMachine_obj = MoneyMachine()

while turn_on:
    prompt = input("What would you like? "+ Menu_obj.get_items() + ": ")

    if prompt == "off":
        turn_on = False
        quit()

    elif prompt == "report":
        CoffeeMaker_obj.report()
        MoneyMachine_obj.report()

    elif prompt == "latte" or prompt == "espresso" or prompt == "cappuccino":
        drink = Menu_obj.find_drink(prompt)
        if CoffeeMaker_obj.is_resource_sufficient(drink):
            if MoneyMachine_obj.make_payment(drink.cost):
                CoffeeMaker_obj.make_coffee(drink)
            else:
                print("Sorry that's not enough money. Money refunded.")






