from data import MENU, resources

def turn_off():
    print("Goodbye! ☕")
    quit()

def report(milk, water, coffee, money):
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")

def money_calculations(quarters, dimes, nickles, pennies, money_need):
    money_total =  int(quarters)*0.5 + int(dimes)*0.1 + int(nickles)*0.05 + int(pennies)*0.01
    if money_total >= money_need:
        diff = money_total - money_need
        print(f"Here is ${round(diff, 2)} in change.")
        return money_need
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0

def goodbye_message(choice):
    print(f"Here is your {choice} ☕. Enjoy!")

milk_left = resources["milk"]
water_left = resources["water"]
coffee_left = resources["coffee"]

def turn_on(milk_left, water_left, coffee_left):
    prompt = input("What would you like? (espresso/latte/cappuccino):")
    money = 0
    money_need = 0

    if prompt == "off":
        turn_off()

    if prompt == "report":
        report(milk_left, water_left, coffee_left, money)
        turn_on(milk_left, water_left, coffee_left)

    if prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        if not prompt == "espresso":
            milk_need = MENU[prompt]["ingredients"]["milk"]
        else:
            milk_need = 0
        water_need = MENU[prompt]["ingredients"]["water"]
        coffee_need = MENU[prompt]["ingredients"]["coffee"]
        money_need = MENU[prompt]["cost"]

        if milk_left < milk_need:
            print("Sorry there is not enough milk.")
            turn_on(milk_left, water_left, coffee_left)
        if water_left < water_need:
            print("Sorry there is not enough water.")
            turn_on(milk_left, water_left, coffee_left)
        if coffee_left < coffee_need:
            print("Sorry there is not enough coffee.")
            turn_on(milk_left, water_left, coffee_left)

        print("Please insert coins.")
        quarters = input("How many quarters?: ")
        dimes = input("How many dimes?: ")
        nickles = input("How many nickles?: ")
        pennies = input("How many pennies?: ")
        money = money_calculations(quarters, dimes, nickles, pennies, money_need)

        if money > 0:
            milk_left -= milk_need
            water_left -= water_need
            coffee_left -= coffee_need
            goodbye_message(prompt)
            turn_on(milk_left, water_left, coffee_left)

turn_on(milk_left, water_left, coffee_left)