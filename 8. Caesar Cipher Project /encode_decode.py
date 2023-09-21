# CAESAR CIPHER ENCODIING PROGRAM

from termcolor import colored
from pyfiglet import Figlet

f= Figlet(font='standard')
print(colored(f.renderText('welcome to my library!'), 'pink'))


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input(" type ' encode ' to encrypt, type 'decode' to decrypt: \n ")
text = input("type your message: ").lower()
shift = int(input("type the shift number: "))
encrypted_message = []
decode_message = []

def caesar():
    if direction=="encode":
        encrypted()
    elif direction =="decode":
        decode()
    else:
        print(" enter a valid choice please. ")
        print(direction)
 # func call       
caesar()

def encrypted():
    for letter in text:
        new_index_num = ( alphabet.index(letter)+shift ) # find the index of the letter in the alphabet list
        new_index = alphabet[new_index_num]
        encrypted_message.append(new_index)
    
    new_message = "".join(encrypted_message)
    print(f"Cipher Text: {new_message}")
    print(f"The encoded text is {new_message} ")


def decode():
    for letter in text:
        new_index_num = ( alphabet.index(letter)-shift ) # find the index of the letter in the alphabet list
        new_index = alphabet[new_index_num]
        decode_message.append(new_index)
    
    new_message = "".join(decode_message)
    print(f"The Text: {new_message}")
    print(f"The  decoded text is {new_message} ")







    




