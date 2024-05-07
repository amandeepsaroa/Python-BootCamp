# here we are only importing the module so when we create object
# we need to specify the moduleName.className
# import turtle
# # objName = moduleName.className()
# tim = turtle.Turtle()


# **************************


# here we are importing specific class from module
# from turtle import Turtle
# # objName = className()
# tim = Turtle()

# **************************

# here we are import everything from module turtle using "*"
# from turtle import *
# tim = Turtle
# this is not recommended in python community coding styles
# this is confusing from where the class is coming


# **************************


# Alias name we can give module a specific name
# using keyword "as"
# import turtle as t
# tim = t.Turtle()

import heroes
print(heroes.gen())
