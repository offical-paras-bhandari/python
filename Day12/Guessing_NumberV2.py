from cmath import log
import random
from art import logo

from turtle import TurtleScreen 

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5 
def check_answer(guess,answer,turns):
    """Check answer against guess. and return numbe of turns happen"""
    if guess > answer:
        print("To High")
        return turns - 1
    elif guess < answer:
        print("To Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")
        
#Make function to set difficulty 
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if(level =="easy"): 
        return EASY_LEVEL_TURN   
    else:
        return HARD_LEVEL_TURN   

def game():  
    #choosing a random number between 1 and 100     
    print(logo)
    print("Welcome to the NUmber Guessing Game!:")
    print("I'm thinking og a number between 1 and 100")
    answer = random.randint(1, 100)

    turns = set_difficulty()

    guess= 0
    while guess!=answer:
        print(f"You have {turns} attemps remaining to guess the number.")

    #Let the User Guess a Number.    
        guess=int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        if(turns==0):
            print("You have {turns} attemps remaining to guess the number")
            return #simply return is used to exit the function
        elif guess!=answer:
            print("Guess again.")
game()