import random
from hangman_word import word_list
from hangman_art import stages , logo
# Step 1

#TODO - 1 Randomly choose a word from the word_list and assign it to a variable called choosen_word
# Create and an empty list called display.
# For each letter in the chosen_word, add a "_" to 'display
# So if the chosen_word was "apple", display should be ["_" , "_" , "_" , "_" , "_"] with 5 "_" representing each letter to guess

# --------------------------------------------------------------------------

#TODO - 2 Ask the user to guess a letter and assign their answer to a varible called guess. Make guess lowercase.
# guessed_letter = input("Guess a letter: ").lower()

# Loop through each position in the chosen_word;
# If the letter at the position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen_word was "apple", then display should be ["_" , "p" , "p" "_" , "_"].

#TODO - 3 Check if the letter the user guessed (guess) is one of the letters in the chosen_word

#Step 4


# Given List
# word_list = ["ardvark" , "baboon" , "camel"]

# Choose random word from given list
print(logo)
chosen_word = random.choice(word_list)
print(f"Word: {chosen_word}")
# display list with number of "_" symbol in it as number of letters in chosen word
display = ["_" for i in range(0 , len(chosen_word))]

# boolean to keep track of is this end of game intially not end of game
end_of_game = False
lives = 6


# run game until not end_of_game or we still have lives left
while not end_of_game:

    guessed_letter = input("Guess a letter: ").lower()
    if guessed_letter in display:
        print(f"You've already guessed {guessed_letter}")
    
    for i in range (0 , len(chosen_word)):
        
        if guessed_letter == chosen_word[i]:
            # print("Right")
            display[i] = guessed_letter

    
    if guessed_letter not in chosen_word:
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lost")  

    print(f"{' '.join(display)}")
    print(stages[lives])
    
    if "_" not in display:
        end_of_game = True
        print("You Win")

     
    