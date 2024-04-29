############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):  # 20 is not included and hence no print is made -> 1....19
#     if i == 20:
#       print("You got it")
# my_function()

# Describe Problem
def my_function():
  for i in range(1, 21):   # 21 is open bracket that it is not included in range only till 20 -> 1.....20
    if i == 20:
      print("You got it")
my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)  # 6 is not a valid index for dice_imgs last index is 5 indexes start at 0  this will produce index error
# print(dice_imgs[dice_num])

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)     # randint(0 , 5) -> here both lower and upper bound are included so these are the indexes as well
print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:  # what is user enters 1994 as year nothing will print there fore we need <= 1994 sign becaue people born in year 1994 are also millenial
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994:   
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")  # and age take it as int
# if age > 18: 
# print("You can drive at age {age}.")  # intendation error and use f string 

# Fix the Errors
age = int(input("How old are you?"))    
if age > 18:
    print(f"You can drive at age {age}.")


# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))   # remove  == that is equality sign it doesnt assign value to variable == will falsify the statement and get 0 in the words_per_page and hence in calculation pages * 0 = 0
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)  # run this line inside for loop to append all the new_item into new b_list 
  print(b_list)

mutate([1,2,3,5,8,13])

