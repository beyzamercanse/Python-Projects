# ROADMAP FOOR THE HANGMAN PROJECT

# 1. ENTER A WORD
# 2. SET AS MUCH BLANK AS THE WORD (LEN(WORD))
# 3. GUESS A LETTER (A-B-C-D-E.......)   
# 4. DOES THE WORD HAS THE LETTER YOOU GUESSED?  
#       -> IF YES : REPLACE THE PLACE OF THE BLANK WITH THE LETTER -> DOES ALL BLANKS ARE FILLED? -> IF YES END THE GAME / IF NO: GO BACK TO THE " GUESS A LETTER "
#       -> IF NO : LOSE A LIFE -> DID YOU RUN OUT OF LIFES? IF YES: END THE GAME / IF NO: GO BACK TO THE "GUESS A LETTER"

# - - - - -  - - 
# - -- - - - -  -
# - -- - - - - - -
# - - -- ----- ---

# for this main1.py file, we will do these first:
# TODO1: RANDOMLY CHOOSE A WORD FROM THE WORD_LIST ASSIGN IT TO THE VARIABLE CALLED CHOSEN_WORD
# TODO2: ASK THE USER TO GUESS A LETTER AND ASSIGN THEIR ANSWER TO A VAR CALLED GUESS. MAKE GUESS LOWVERCASE.
# TODO3: CHECK IF THE LETTER THE USER GUESSED IS ONE OF THE LETTERS IN THE CHOSEN_WORD.
import random 

def hangman():
    word_list = ["adjavent", "enormous","majesty"]
    chosen_word = random.choice(word_list) #todo1

    guess = (input("Guess a letter: ")).lower() #todo2

    for letter in chosen_word: #todo3
        if guess == letter:
            print("right")
        else:
            print("wrong")

    

hangman()






