#Calcualtor 
#TODO - ADD
def add(n1,n2):
    return n1+n2

#TODO - Subtract
def subtract(n1,n2):
    return n1-n2

#TODO - Multiple
def multiply(n1,n2):
    return n1*n2

#TODO - Divide
def divide(n1,n2):
    return n1/n2

Opereations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

num1 = int(input("What's the first number?: "))
num2= int(input("What's the second number?: "))

for symbol in Opereations:
    print(symbol)
    
operation_symbol = input("Pick ans operation from the line above: ")
if operation_symbol == "+":
    """So, + symbol is choosen then key: + is activated and due to line 34 [key "+" ]
    value:- Add is activated  which is function so this function is hold by calculation_function which act as Add() function 
    here we have two parameter num1,num2 because add function is return type (Function with output) so we have to hold the answer So,
    we have hold the aswer by answer variable"""
    calculation_function = Opereations[operation_symbol]#(num1, num2)
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
Shouldcontinue=True
while Shouldcontinue:
    user_choice = input(f"Type 'y' to continue calculating {answer}, or type 'n' to exit.: ")
    if(user_choice=="y"):        
        operation_symbol = input("Pick an operation from the line above: ")       
        if operation_symbol == "+":
            num3= int(input("What's the next number?: "))
            calculation_function = Opereations[operation_symbol]#(num1, num2)
            updated_answer = calculation_function(answer, num3)
            print(f"{answer} {operation_symbol} {num3} = {updated_answer}")
    else:
        Shouldcontinue=False    
# elif operation_symbol == "-":
#     calculation_function = Opereations[operation_symbol]#(num1, num2)
#     answer = calculation_function(num1, num2)
# elif operation_symbol == "*":
#     calculation_function = Opereations[operation_symbol]#(num1, num2)
#     answer = calculation_function(num1, num2)
# else:
#     calculation_function = Opereations[operation_symbol]#(num1, num2)
#     answer = calculation_function(num1, num2)
# answer(num1, num2)
    
