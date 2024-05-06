from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# creating object of different classes
drinkObject = Menu()
coffeeObject = CoffeeMaker()
moneyObject = MoneyMachine()

# infinite loop
while True:

    # get the user input and print the menu using the Menu object
    user_choice = input(f"What would you like? ({drinkObject.get_items()}): ").lower()

    # if user says off then end the loop
    if user_choice == 'off':
        break

    # otherwise if user says to print the report
    # First print the ingredients summary using the CoffeeMaker Object
    # Then print the profit using the MoneyMachine object
    # and continue taking the input from the user for that go to the start of the loop again
    elif user_choice == 'report':
        coffeeObject.report()
        moneyObject.report()
        continue

    # else start processing the drink if valid user_choice
    else:

        userDrinkObject = drinkObject.find_drink(user_choice)

        if userDrinkObject:
            # check if we have enough resources
            if coffeeObject.is_resource_sufficient(userDrinkObject):

                # take money and check if enough money given
                if moneyObject.make_payment(userDrinkObject.cost):
                    coffeeObject.make_coffee(userDrinkObject)
                else:
                    print("False")
        else:

            # if its not a valid choice function will print the error you just continue taking the input
            continue




