# CAESAR CIPHER

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input(" type ' encode ' to encrypt, type 'decode' to decrypt: \n ")
text = input("type your message: ").lower()
shift = int(input("type the shift number: "))
encrypted_message = []

# code below
# todo1: create a function called 'encrypt' that takes the text and shift as inputs.
# todo2: do the shift
# todo3: call encrypt message

def encrypted():
    for letter in text:
        new_index_num = ( alphabet.index(letter)+shift ) # find the index of the letter in the alphabet list
        new_index = alphabet[new_index_num]
        encrypted_message.append(new_index)
    
    new_message = "".join(encrypted_message)
    print(f"Cipher Text: {new_message}")
    print(f"The encoded text is {new_message} ")

encrypted()

def encrypted_two():
    # this is 2nd solutiion approach to the encrypting
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position+shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text} ")













