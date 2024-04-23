#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



generatedPassword_list = []

# add random nr_letters number of  letters to list
for char in range(0 , nr_letters):
    generatedPassword_list.append(random.choice(letters))

# add random nr_symbols number of  symbols to list
for char in range(0 , nr_symbols):
    generatedPassword_list.append(random.choice(symbols))

# add random nr_numbers number of  number to list
for char in range(0 , nr_numbers):
    generatedPassword_list.append(random.choice(numbers))

# now to generate random password shuffle the list ie take random element one by one and create string
generatedPassword_str = ''

for char in range(0 , len(generatedPassword_list)):
    # taka random index from the list and pop that element and add to string password 
    # do this till your list gets empty therefore all the characters are used from the list and your condition also met

    generatedPassword_str += generatedPassword_list.pop( random.randint(0 , len(generatedPassword_list) - 1) )

    # or you can use shuffle method in random to shuffle the list and then make str after that
    ## generatedPassword_list = random.shuffle(generatedPassword_list)

print(generatedPassword_str)