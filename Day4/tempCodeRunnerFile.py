
# if both user and computer choose same there thats a draw
if user_choice == computer_choice:
    print(f"It's a draw")
elif user_choice == 1 and computer_choice == 2:
    print(f"You lose")
elif user_choice == 2 and computer_choice == 0:
    print(f"You lose")
else:
    print("You win")