#Step 1 
import random
from tkinter import TRUE
word_list = ["aardvark", "baboon", "camel"]






choosen_name=""
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
choosen_name=word_list[random.randint(0,len(word_list)-1)]
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess= input("Enter a letter: ").lower()
print(choosen_name)
for n in range(random.randint(0,len(choosen_name)-1)):
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    if(choosen_name[n]==guess):
        choosen_name=TRUE
if(choosen_name!=TRUE):
    print("invalid")
else:
    print("valid")
    



       
      



