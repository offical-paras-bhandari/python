#Number Guessing Game Objectives:
import random

# Include an ASCII art logo.
from art import logo 
print(logo)
# Allow the player to submit a guess for a number between 1 and 100.
print("Welcome to the Number Guessing Game!")
def guessed_Number():
    Guessing_Number = random.randint(1, 100)
    return Guessing_Number
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
print("I'm thinking of number between 1 and 100")
def guessing_Number(guss_number,random_guessed_Number):
# If they got the answer correct, show the actual answer to the player.        
        if(guss_number >random_guessed_Number):
            return ("You have guessed to high")
        elif(guss_number < random_guessed_Number):
            return ("You have guessed to low")
        else:
            return (f"You have guessed Correct {guss_number}")
            
def gamedificulty(level,random_guessed_Number):
    easy = 10
    hard = 5
    if(level == "easy"):
        finished =False
        while not finished:
            print(f"your have {easy} atttemps remaning to guess the number.")
            player_guess=int(input("Make a guess: "))
            checking=guessing_Number(player_guess,random_guessed_Number)
            print(checking)
            
            # Track the number of turns remaining.
            if(player_guess!=random_guessed_Number):
                easy-=1
                if(easy==0):
                     print(f"your have {easy} atttemps.")
                     finished=True
            else:
                finished=True
        # If they run out of turns, provide feedback to the player.                        
        
    else:
        finished =False
        while not finished:
            print(f"your have {hard} atttemps remaning to guess the number.")
            player_guess=int(input("Make a guess: "))
            checking=guessing_Number(player_guess,random_guessed_Number)
            print(checking)
            
            # Track the number of turns remaining.
            if(player_guess!=random_guessed_Number):
                hard-=1
                if(hard==0):
                    print(f"your have {hard} atttemps.")
                    finished=True
            else:
                finished=True 

guess_Number=0
random_guessed_Number = guessed_Number()
print(f"pssst, tte correct answer is {random_guessed_Number}")
level = input("Choose a difficulty. Type 'easy' or 'hard': ") 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
game_level=gamedificulty(level,random_guessed_Number)
