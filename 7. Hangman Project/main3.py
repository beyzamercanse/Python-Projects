
import random
word_list = ["vienna", "amsterdam","london", "berlin", "norway"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

def hangman():
    display = []

    # TODO1: assign the display list
    for letter in chosen_word:
        display.append("_")
    print(display)

    # 1 : USE A WHILE LOOP TO LET THE USER GUESS AGAIN. 
    # THE LOOP SHOULD ONLY STOP ONCE THE USER HAS GUESSED ALL THE LETTERS IN THE CHOSEN_WORD 
    # AND "DISPLAY" HAS NO MORE BLANKS "-" SO YOU CAN TELL THE USER THEY WON.

    end_game = False

    while not end_game: 
        guess = input(" guess a letter:  ").lower()
        # check the guessed
        for position in range(word_length):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = letter
        print(display) 

        if "_" not in display:
            end_game = True
            print(" you won!")


        
hangman()