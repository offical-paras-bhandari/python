from art import logo, vs
from game_data import data
import random
import os


def clear():
    os.system('cls')
# Display art


print(logo)
# Score Keeping.
score = 0
game_should_continue = True
account_b = random.choice(data)
# Make the game repeatable.
while game_should_continue:
    
    # Format the account data into printable. 
    def format_data(account):
        """Takes the account data and returns the printable format."""
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]
        return f"{account_name}, a{account_descr}, a{account_country}"

    def check_answer(guesses, a_follower, b_follower):
        """Takes the user guess and follower counts and returns if they got it right."""
        if a_follower > b_follower:
            return guesses == "a"   #Returns , Evaluating True or False.
        else:
            return guesses == "b"   #Returns , Evaluating
        
    # Generate a random accounts from the data.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A: {format_data(account_a)}")#here no need to hold the data, as we can hold data.
    print(vs)
    print(f"Compare A: {format_data(account_b)}")

    # Ask user for a guess.
    guess = input("Who has more follower? Type 'A' or 'B': ").lower()
    # Check if user is correct.
    # follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # Use if statement to check if user is correct.
    if is_correct:#This is true
        score += 1
        print(f"you are right! Current Score : {score} ")
        
    # Give user feedback on their guess.
        clear()
    else:
        print(f"you are Wrong! Final Score : {score} ")
        game_should_continue = False
