import os
import random
from day_Hangman_art import logo
from day_Hangman_art import stages
from day_Hangman_words import word_list


def cls():
    os.system('cls')


print(logo)

chosen_word = random.choice(word_list)
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
chosen_word_len = len(chosen_word)
for _ in range(chosen_word_len):
    display.append("_")

game_over = False
isLetterInRange = False

user_result = ' '.join(display)

while not game_over:
    guess = input("Guess a letter: ").lower()

    cls()

    if guess in ''.join(display):
        print("")
        print(f"Letter [{guess}] is already guessed")

    for i in range(chosen_word_len):
        if chosen_word[i] == guess:
            display[i] = guess
            isLetterInRange = True

    if "_" not in display:
        game_over = True
        print("You won!")

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter [{guess}] is not in the word")

        if lives == 0:
            game_over = True
            print("You lose!")

    isLetterInRange = False

    print("")
    print(f"{' '.join(display)}")
    print(stages[lives])
