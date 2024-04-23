# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
sumHeight = 0
numberOfStudents = 0
for height in student_heights:
  sumHeight += height
  numberOfStudents += 1

print(f'total height = {sumHeight}')
print(f'number of students = {numberOfStudents}')
print(f'average height = {round( (sumHeight) / numberOfStudents )}')
  