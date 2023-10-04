import random
from art import logo

game_over = False


def print_welcome_message():
    print(logo)
    print(" 💪🏻💪🏻💪🏻  Welcome to the number guessing game!  💪🏻💪🏻💪🏻 ")
    print("👩🏻‍💻👩🏻‍💻👩🏻‍💻 I am thinking of a number between 1 and 100. 👩🏻‍💻👩🏻‍💻👩🏻‍💻 ")


def get_user_guess():
    while not game_over:
        try:
            user_guess = int(input("Make a guess: "))
            return user_guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def play_game():
    computer_guess = random.randint(1, 100)
    number_of_attempts = 0
    print_welcome_message()
    difficulty = input("Choose a difficulty: 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        number_of_attempts = 10
    elif difficulty == 'hard':
        number_of_attempts = 5
    else:
        print("Invalid difficulty level. Defaulting to easy.")
        number_of_attempts = 10

    while number_of_attempts > 0:
        print(
            f"You have {number_of_attempts} attempts remaining to guess the number.")
        user_guess = get_user_guess()

        if user_guess > computer_guess:
            print("Too high!")
        elif user_guess < computer_guess:
            print("Too low!")
        else:
            print(f"You guessed right! The correct number is {user_guess}.")
            return

        number_of_attempts -= 1

    print(f"Game over! The correct number was {computer_guess}.")


def play_again():
    while not game_over:
        again = input("Do you want to play again? (yes/no): ").lower()
        if again == 'yes':
            play_game()
        elif again == 'no':
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    play_game()
    play_again()
