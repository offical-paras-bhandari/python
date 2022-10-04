from turtle import pos, position


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text, shift_amount):
# #     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
oldPlainText=""
newPlainText =""
def ceasar(direction,text,shift):
    def encrypt(plain_text, shift_amount):    
   
        for letter in plain_text:
            postion=alphabet.index(letter)
            new_postion=shift_amount + postion#TODO - addming amound to index
            newPlainText+=alphabet[new_postion]
    print(f"The decoded plain text is {newPlainText}")
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    def decrypt(cipher_text, shift_amount):
        
        for letter in cipher_text:
            newPlainText=alphabet.index(letter)#get the index of an item in a list:
            new_postion=newPlainText-shift_amount#TODO - addming amound to index
            oldPlainText+=alphabet[new_postion]
    print(f"The decoded plain text is {oldPlainText}")
    #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
    if direction=="encode":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction=="decode":
        decrypt(cipher_text=text, shift_amount=shift )

    
    
    
    

