
import random
word_list = ["vienna", "amsterdam","london", "berlin", "norway"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# TODO1 : CREATE A VAR CALLED AS "LIVES" TO KEEP A TRACK OF THE NUMBER OF LIVES LEFT.
# SET LIVES TO 6 

def hangman():
    display = []

    # assign the display list
    for letter in chosen_word:
        display.append("_")
    print(display)

# TODO2: IF GUESS IS NOT A LETTER I THE CHOSEN WORD, REDUCE LIVES VAR BY 1. IF LIVES = 0, THE GAME SHOULD STOP AND YOU SHOULD PRINT "YOU LOST"

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