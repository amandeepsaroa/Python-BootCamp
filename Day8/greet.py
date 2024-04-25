def greet():

    print(f'Hello')
    print(f'How do you do?')
    print(f"Isn't the weather nice today?")


greet()

#Function that allow for input
def greet_with_name(name):
    
    print(f'\n\nHello, {name}')
    print(f'How do you do {name}?')
    print(f"{name} isn't the weather nice today?")

greet_with_name("Angela")


def greet_with(name , location):

    print(f'\n\nHello, {name}\nWhat is it like in {location}')

greet_with("Angela Yu" , "London")