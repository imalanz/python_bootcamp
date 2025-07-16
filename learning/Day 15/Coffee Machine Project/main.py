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

money = 0
completed = True
while completed:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee == 'off':
        completed = False
    if coffee == 'report':
        print(resources)

    for ingredient, value in MENU[coffee]["ingredients"].items():
        if resources[ingredient] > value:
            resources[ingredient] -= value
        else:
            print(f"Sorry, there is not enough {ingredient}")
            completed = False

    print(resources)
    if completed == True:
        coffe_cost = MENU[coffee]["cost"]
        print(f"coffee cost is: {coffe_cost}")

        quarters = int(input("how many quarters: ")) * 0.25
        dimes = int(input("how many dimes: ")) * 0.10
        nickles = int(input("how many nickles: ")) * 0.05
        pennies = int(input("how many pennies: ")) * 0.01

        total_money = quarters + dimes + nickles + pennies
        if total_money < coffe_cost:
            print("Sorry that is not enough money.")
            completed = False
        elif total_money >= coffe_cost:
            refund = round(total_money - coffe_cost, 2)
            if refund > 0:
                print(f"Your change is: {refund}")
            money += coffe_cost
            print("Your coffee is preparing")
            print(money)







