from os import system, name
# import sleep to show output for some time period
from time import sleep
# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
#Game state
game_is_finished = False
#Total stages are 7
lives = len(stages) - 1
#Randomly choses a word
chosen_word = random.choice(word_list)
#Stores the word's length
word_length = len(chosen_word)
#Creates an empty list
display = []
#Adds _ to the empty list
for _ in range(word_length):
    display += "_"
#Main program
while not game_is_finished:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")
    #Checks if the guessed letter is in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            #Replaces _ in display with the letter
            display[position] = letter
    #Join all the elements in the list and turn it into a string
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    #All letters are guessed by the player
    if not "_" in display:
        game_is_finished = True
        print("You win.")
    #prints each stage corresponding to the lives remaining
    print(stages[lives])