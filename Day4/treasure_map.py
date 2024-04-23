line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


# extract column number from the input string 
# here 0th element in string is the column number so assign specific index based on the column alphabet
m = position[0]
if m.lower() == 'a':
  column = 0
elif m.lower() == 'b':
  column = 1
else:
  column = 2

# get row number from string which is at 1st index of input string
# convert to string so that we can use it as index
row = int(position[1]) 

# now place the X mark at specific cell
# we are doing row - 1 because given input user string consider 1 , 2 , 3 as row numbers but 
# to access 1st row you need to go to 0th index of map list 0th index will take you to list1 and then column number will take you to the specific element in list1 at that index
map[row - 1][column] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")