import random
from art import logo

print(logo)
print(" 💪🏻💪🏻💪🏻  Welcome to the number guessing game!  💪🏻💪🏻💪🏻 ")
print("👩🏻‍💻👩🏻‍💻👩🏻‍💻 I am thinking of a number between 1 and 100. 👩🏻‍💻👩🏻‍💻👩🏻‍💻 ")
computer_guess = random.randint(0, 100)


def game():
    game_over = False

    def hardness(difficulty):
        if difficulty == 'easy':
            attempt = 10
        elif difficulty == 'hard':
            attempt = 5
        return attempt

    level = input("Choose a difficulty: 'easy' or 'hard? :      ")
    number_of_attempt = hardness(level)

    while not game_over:
        print(
            f"you have {number_of_attempt} number of attempts remaining to guess the number.")
        number_of_attempt -= 1

        if number_of_attempt > -1:
            user_guess = int(input("Make a guess: "))
            if user_guess > computer_guess:
                print("too high!")
                print("guess_again")
            elif user_guess == computer_guess:
                print("you guessed right!")
                print(f"correct number is {user_guess}.")
                game_over = True
            elif user_guess < computer_guess:
                print("too low!")
                print("guess_again")
        else:
            print("game over")
            game_over = True


game()
