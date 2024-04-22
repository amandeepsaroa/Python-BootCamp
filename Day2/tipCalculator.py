print(f'Welcome to the tip calculator!')
totalbill = float(input('What was the total bill? '))
tipPercent = float(input('How much tip would you like to give? 10, 12, or 15? '))
totalPeople = float(input('How many people to split the bill? '))

billPerPerson = ( totalbill + (totalbill * (tipPercent/100)) ) / totalPeople
print(f'Each person should pay: ${round(billPerPerson , 2)}')