import random 


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


thisdict = {
  0: rock,
  1: paper,
  2: scissors
}
user_choice = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(thisdict[user_choice])

computer_choice = random.randint(0 , 2) # random number between 0 .. 2 (both included)
print(f'Computer choose: {thisdict[computer_choice]}')

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!")

# if both user and computer choose same there thats a draw
if user_choice == computer_choice:
    print(f"It's a draw")

# Only Loosing Case
elif user_choice == 1 and computer_choice == 2:
    print(f"You lose")
elif user_choice == 2 and computer_choice == 0:
    print(f"You lose")
elif user_choice == 0 and computer_choice == 1:
    print(f"You lose")
# Rest is Winning Case
else:
    print("You win")