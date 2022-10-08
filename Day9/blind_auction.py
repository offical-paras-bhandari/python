import imp
from art import logo
import os
def clear():
    os.system('cls')
print (logo)
print("Welcome to the secret aution program")

def blind_auction(Name, Bid):
    blind_auction_list[Name] = Bid
blind_auction_list = {}   


shouldContiue=True
while shouldContiue:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    halt=input("Are there any other jbidders? Type 'yes' or 'no'.")
    if halt=="no":
        shouldContiue=False
    clear()
    blind_auction(Name=name, Bid=bid)  

    
higestbid =0
for bidder_name in blind_auction_list:
    bid = blind_auction_list[bidder_name]
    if(bid > higestbid):
        higestbid = bid
    
print(f"The winner is {bidder_name} with bid of ${higestbid}")
print(blind_auction_list)