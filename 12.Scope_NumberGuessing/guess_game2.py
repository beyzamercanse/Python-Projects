import random
from art import logo

print(logo)
print(" 💪🏻💪🏻💪🏻  Welcome to the number guessing game!  💪🏻💪🏻💪🏻 ")
print("👩🏻‍💻👩🏻‍💻👩🏻‍💻 I am thinking of a number between 1 and 100. 👩🏻‍💻👩🏻‍💻👩🏻‍💻 ")
computer_guess = random.randint(0, 100)
game_over = False


def game():
    global game_over

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

        if number_of_attempt > 0:
            user_guess = int(input("Make a guess: "))
            if user_guess > computer_guess:
                print("too high!")
                print("guess again")
            elif user_guess == computer_guess:
                print("you guessed right!")
                print(f"correct number is {user_guess}.")
                game_over = True
            elif user_guess < computer_guess:
                print("too low!")
                print("guess again")
        else:
            print("game over")
            game_over = True


def play_again():
    while True:
        again = input("Do you want to play again? (yes/no): ").lower()
        if again == 'yes':
            game()
        elif again == 'no':
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")


game()
play_again()
