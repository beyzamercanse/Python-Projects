

# STEP 2
import random
word_list = ["vienna", "amsterdam","london", "berlin", "norway"]
chosen_word = random.choice(word_list)

# testing code
print(f"the solution is {chosen_word}")

# todo1 : CREATE AN EMPTY LIST CALLED DISPLAY, FOR EACH LETTER INN THE CHOSEN_WORD, ADD A "-" TO DISPLAY.
# todo2 : loop through each position in the chosen_word, 
# if the letter that position matches "guess" then reveal the letter in the display at that position.
# if the user guessed "p" and the chosen word was "apple", then display should be ["-","p","p","-","-"]

#todo3: print"display" and you should see the guessed letter in the correct position and every other letter replaced with "-"

def hangman():
    display = []

    # TODO1: ssign the display list
    for letter in chosen_word: # or for letter in range(len(chosen_word))
        display.append("-")
    print(display)

    # guess the letter
    guess = input("enter a letter: ").lower()

    # TODO2, we have to index the letter in the display list to find the letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    print(display) #todo3




        


    
    
 



hangman()



