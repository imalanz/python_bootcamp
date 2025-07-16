from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
while is_on:
    choice = input(f"What would you like? {Menu().get_items()}: ")
    if choice == 'off':
        is_on = False
    elif choice = 'report':
        CoffeeMaker().report()
        MoneyMachine().report()
    else:
        drink = Menu().find_drink(choice)
        if is_resource_sufficient(drink):
            if MoneyMachine().make_payment(drink.cost) and CoffeeMaker().is_resource_sufficient(drink):

                CoffeeMaker().make_coffee()

