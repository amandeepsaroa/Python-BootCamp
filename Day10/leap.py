def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year , month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    
    # in leap year only Feb have 29 days rest month have same days in month
    # so if leap year and user passed month as 2 which is Feb we will just add 1 to 28 
    # to access the number of days in list of month_days use month number as index but do - 1 because index start from 0
    # so if user passed month = 3 that is March therefore to access the number of days in month in list days_in_month get to 2nd index which is 3rd element 
    # days_in_month[month - 1]
    if is_leap(year) and month == 2:
      return month_days[month - 1] + 1
    else:
      return month_days[month - 1]

    
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

