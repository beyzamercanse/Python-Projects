# CAESAR CIPHER

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(" type ' encode ' to encrypt, type 'decode' to decrypt: \n ")
text = input("type your message:\n").lower()
shift = int(input("type the shift number: \n"))

# code below
# todo1: create a function called 'encrypt' that takes the text and shift as inputs.
# todo2: do the shift


def encrypt(text, shift):

    positions = []
    for letter in text:
        position = alphabet.index(letter)
        positions += position

    print(positions)


encrypt(text, shift)
