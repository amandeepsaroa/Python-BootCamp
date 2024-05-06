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
    "money": 0.00
}

coins = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0
}


def print_report(current_resources):
    print(f"Water: {current_resources['water']}ml\nMilk: {current_resources['milk']}ml\nCoffee: {current_resources['coffee']}g\nMoney: ${current_resources['money']}")


def process_coffee(user_choice):

    if user_choice == 'espresso':
        resources['water'] -= MENU[user_choice]['ingredients']['water']
        resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']
    else:

        resources['water'] -= MENU[user_choice]['ingredients']['water']
        resources['milk'] -= MENU[user_choice]['ingredients']['milk']
        resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']


def process_coins(user_choice):

    money_received = (coins['quarters'] * 0.25) + (coins['dimes'] * 0.10) + (coins['nickles'] * 0.05) + (
                 coins['pennies'] * 0.01)
    change = money_received - MENU[user_choice]['cost']

    resources['money'] += MENU[user_choice]['cost']

    return change


def have_sufficient_resources(user_choice):

    if MENU[user_choice]['ingredients']['water'] >= resources['water']:
        print(f"Sorry there is not enough water.")
        return False
    elif user_choice != 'espresso' and MENU[user_choice]['ingredients']['milk'] >= resources['milk']:
        print(f"Sorry there is not enough milk.")
        return False
    elif MENU[user_choice]['ingredients']['coffee'] >= resources['coffee']:
        print(f"Sorry there is not enough coffee.")
        return False
    else:
        return True


def have_sufficient_money(user_choice):
    # resources['money'] = (coins['quarters'] * 0.25) + (coins['dimes'] * 0.10) + (coins['nickles'] * 0.05) + (coins['pennies'] * 0.01)
    total_money = (coins['quarters'] * 0.25) + (coins['dimes'] * 0.10) + (coins['nickles'] * 0.05) + (coins['pennies'] * 0.01)

    if total_money >= MENU[user_choice]['cost']:

        return True

    else:

        print(f"Sorry that's not enough money. Money refunded")
        return False


def main():

    while True:

        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_choice == 'off':
            break

        elif user_choice == 'report':

            print_report(resources)
            continue

        else:

            if have_sufficient_resources(user_choice):

                print("Please insert coins")
                coins['quarters'] = int(input("How many quarters?: "))
                coins['dimes'] = int(input("How many dimes?: "))
                coins['nickles'] = int(input("How many nickles?: "))
                coins['pennies'] = int(input("How many pennies?: "))

                if have_sufficient_money(user_choice):
                    # if have_sufficient_money(user_choice) and have_sufficient_resources(user_choice):
                    process_coffee(user_choice)
                    change = process_coins(user_choice)

                    print(f"Here is ${change:.2f} in change.")
                    print(f"Here is your {user_choice} ☕ Enjoy!")


if __name__ == "__main__":
    main()
# print_report(resources)
