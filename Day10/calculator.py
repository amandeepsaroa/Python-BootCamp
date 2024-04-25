from art import logo
import os

# Calculator

# Add
def add(a , b):
    return a + b

# Divide
def divide(a , b):
    return a / b

# Multiply
def multiply(a , b):
    return a * b

# Subtract
def subtract(a , b):
    return a - b



operation_dict = { "+" : add , "-" : subtract , "*" : multiply , "/" : divide}
state = 'n'


def calculator():
    
    print(logo)
    should_continue = True  
    a = float( input("What's the first number?: ") )
    for symbol in operation_dict:
            print(symbol)

    while should_continue:

        choosen_operation = input("Pick an operation: ")
        b = float( input("What's the next number?: ") )
        result = operation_dict[choosen_operation](a , b)

        print(f"{a} {choosen_operation} {b} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
             a = result
        else:
            # using recursion
            should_continue = False
            os.system('cls')
            calculator()


calculator()