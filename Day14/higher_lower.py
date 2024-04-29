import random
from game_data import data
import os
from art import logo , vs

current_score = 0

while True:

    print(logo)
    if current_score != 0:
        print(f"You're right! Current Score: {current_score}")
    
    # random.sample will generate 2 different random number betwenn the given range
    random_index_list = random.sample( range(0 , len(data) - 1), 2 )

    dict_A = data[random_index_list[0]]
    dict_B = data[random_index_list[1]]

    print(f"Compare A: { dict_A['name'] }, { dict_A['description'] } , from { dict_A['country'] }.")
    print(vs)
    print(f"Against B: { dict_B['name'] }, { dict_B['description'] } , from { dict_B['country'] }.")


    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    os.system('cls')

    if user_choice == 'a' and dict_A['follower_count'] > dict_B['follower_count']:
        current_score += 1
    elif user_choice == 'b' and dict_B['follower_count'] > dict_A['follower_count']:
        current_score += 1  
    else:
        print(f"Sorry, that's wrong. Final Score: {current_score}")
        break

    