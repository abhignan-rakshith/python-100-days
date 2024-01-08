from logo import art
from time import sleep
from os import system
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MONEY = 0
is_on = True

menu = Menu()
coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()


def can_make_coffee():
    return True


print(art)
while is_on:
    user_command = input(f"\nWhat would you like? >> {menu.get_items()}\n"
                         ">> report\n>> off\n----->").lower()

    if user_command == "report":
        sleep(1)
        coffeeMachine.report()
        moneyMachine.report()

    elif user_command == "off":
        is_on = False

    else:
        coffee = menu.find_drink(user_command)

        if coffee is None:
            sleep(2)
            system('cls')

        else:
            available_resource = coffeeMachine.is_resource_sufficient(coffee)
            print("Lets make coffee!\n")
            if available_resource:
                transaction_successful = moneyMachine.make_payment(coffee.cost)
                if transaction_successful:
                    print("\nMaking Coffee...")
                    sleep(2)
                    coffeeMachine.make_coffee(coffee)

system('cls')
w = input("Press 'ENTER' to exit...")
