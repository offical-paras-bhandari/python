from art import logo
import os
def clear():
    os.system('cls')
print (logo)

def calcualtions(first_number,pick_operations,next_number):
    if(pick_operations =="+"):
        return float(first_number + next_number)
    elif(pick_operations =="-"):
        return float(first_number - next_number)
    elif(pick_operations =="*"): 
        return float(first_number * next_number)
    elif(pick_operations == "/"):
        return float(first_number / next_number)        
    
shouldcalcualted=True
again_calculated=True
while shouldcalcualted:
    first_number = int(input("What's the first number?: "))
    print ("+ \n- \n* \n/ ")
    pick_operations = input("Pick an Opereation: ")
    next_number = int(input("What's the next number?: "))   
    calculated=calcualtions(first_number, pick_operations ,next_number)
    print (f"{first_number} {pick_operations} {next_number} = {calculated}")
    user_choice=input("Type 'y' to continue calculating with 10.0 or type 'n' to start a new calcualtion: ")
    if user_choice=="n":
        clear()
        first_number = int(input("What's the first number?: "))
        print ("+ \n- \n* \n/ ")
        pick_operations = input("Pick an Opereation: ")
        next_number = int(input("What's the next number?: "))   
        calculated=calcualtions(first_number, pick_operations ,next_number)
        print (f"{first_number} {pick_operations} {next_number} = {calculated}")
        user_choice=input("Type 'y' to continue calculating with 10.0 or type 'n' to start a new calcualtion: ")
    else:
        while again_calculated:
            pick_operations = input("Pick an Opereation: ")
            next_number = int(input("What's the next number?: "))   
            calculated=calcualtions(calculated, pick_operations ,next_number)    
            print (f"{calculated} {pick_operations} {next_number} = {calculated}")
            user_choice=input("Type 'y' to continue calculating with 10.0 or type 'n' to start a new calcualtion: ")
            if(user_choice=='n'):
                again_calculated=False    
            clear()    
                    