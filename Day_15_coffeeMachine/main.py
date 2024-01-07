import logo
from time import sleep
from os import system
from menu import MENU, resources


def is_resource(ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    if (resources['water'] <= ingredients['water'] or resources['milk'] <= ingredients['milk'] or
            resources['coffee'] <= ingredients['coffee']):
        for ITEM in ingredients:
            if ingredients[ITEM] > resources[ITEM]:
                print(f"Sorry there is not enough {ITEM}.")
        return False
    return True


def coin_processing():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    inputMoney = int(input("how many quarters?: ")) * 0.25
    inputMoney += int(input("how many dimes?: ")) * 0.1
    inputMoney += int(input("how many nickles?: ")) * 0.05
    inputMoney += int(input("how many pennies?: ")) * 0.01
    return inputMoney


def is_transaction_successful(amount, coffee_price):
    """Return True when the payment is accepted, or False if money is insufficient."""
    # TODO: 6. Add money to the machine.
    if amount >= coffee_price:
        change = round(amount - coffee_price, 2)
        print(f"Here is ${change} in change.")
        global MONEY
        MONEY += coffee_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(coffee_name, ingredients):
    """Deduct the required ingredients from the resources."""
    for ITEM in ingredients:
        resources[ITEM] -= ingredients[ITEM]
    print(f"Here is your {coffee_name} ☕️. Enjoy!")


MONEY = 0
isOn = True

print(logo.art)
while isOn:
    # TODO: 1. Print report of all coffee machine resources
    userCommand = input("\nWhat would you like?\ntype (espresso/latte/cappuccino)\n"
                        "type 'report'\ntype 'menu'\n----->").lower()

    menuList = ["espresso", "latte", "cappuccino"]
    if userCommand == "report":
        sleep(1)
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\n"
              f"Coffee: {resources["coffee"]}g\nMoney: ${MONEY}\n")

    # TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    elif userCommand == "off":
        sleep(1)
        isOn = False

    # TODO: 7. Show MENU of the Coffee Machine by entering “ menu ” to the prompt.
    elif userCommand == "menu":
        sleep(1)
        for item in MENU:
            print(f"{item}: ${MENU[item]['cost']}")

    elif userCommand not in menuList:
        print("Invalid Command...")
        sleep(1)
        isOn = False

    else:
        # TODO: 3. Check resources sufficient?
        coffee = MENU[userCommand]
        availableResource = is_resource(coffee["ingredients"])
        if availableResource:
            # TODO: 4. Process coins.
            total = coin_processing()
            transaction_successful = is_transaction_successful(amount=total, coffee_price=MENU[userCommand]['cost'])

            if transaction_successful:
                # TODO: 5. Make Coffee.
                sleep(2)
                make_coffee(userCommand, coffee["ingredients"])

system('cls')
w = input("Press 'ENTER' to exit...")
