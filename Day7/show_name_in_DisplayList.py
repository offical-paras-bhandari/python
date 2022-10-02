#Step 1 
import random
import HangMan_art
import HangMan_word
from stat import UF_APPEND

from tkinter import TRUE
word_list = ["apple", "baboon", "camel"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
choose_word=random.choice(word_list).lower()
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess =input("Guess a letter: ").lower()

#TODO-1: - Create an empty List called display.
display_list=[]
#TODO - For each letter in the chosen_word, add a "_" to 'display'.
iscorrect=""
for i in range(len(choose_word)):
    display_list.append(["_"])#TODO - this-> is also ok display_list+="_"
#TODO - So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
#TODO-2: - Loop through each position in the chosen_word;
#TODO - If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#TODO - e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for position in range(len(choose_word)):
    if(choose_word[position]== guess):
        display_list[position] = guess
        iscorrect = True

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
if(iscorrect==True):
    print(display_list)
else:
    print("Your guess was incorrect")
