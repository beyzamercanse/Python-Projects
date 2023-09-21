# CAESAR CIPHER ENCODIING PROGRAM

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input(" type ' encode ' to encrypt, type 'decode' to decrypt: \n ")
text = input("type your message: ").lower()
shift = int(input("type the shift number: "))
decode_message = []

# code below
# todo1: create a function called 'decode' that takes the text and shift as inputs.
# todo2: do the shift
# todo3: call decoded message

def decode():
    for letter in text:
        new_index_num = ( alphabet.index(letter)-shift ) # find the index of the letter in the alphabet list
        new_index = alphabet[new_index_num]
        decode_message.append(new_index)
    
    new_message = "".join(decode_message)
    print(f"The Text: {new_message}")
    print(f"The  text is {new_message} ")

decode()


