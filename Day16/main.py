from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinkObject = Menu()
coffeeObject = CoffeeMaker()
moneyObject = MoneyMachine()

while True:

    user_choice = input(f"What would you like? ({drinkObject.get_items()}): ").lower()

    if user_choice == 'off':
        break

    elif user_choice == 'report':
        coffeeObject.report()
        moneyObject.report()
        continue

    else:

        userDrinkObject = drinkObject.find_drink(user_choice)

        # check if we have enough resources
        if coffeeObject.is_resource_sufficient(userDrinkObject):

            # take money and check if enough money given
            if moneyObject.make_payment(userDrinkObject.cost):
                coffeeObject.make_coffee(userDrinkObject)
            else:
                print("False")




