# display first art

# compare a:
# display second art
# against b:

# who has more followers? "A" or "B"?

# repeat :
# sorry you are wrong , 0 - exit
# you are right! 1,2,3, point
# if you are right, now the higher one becomes option A , continue


import random
from art import logo, vs
from game_data import data
from replit import clear


def get_random_account():
    """Get data from random account"""
    return random.choice(data)


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account['name']
    description = account['name']
    country = account['country']
    return f"{name}, a {description}, from {country}"


# list = [{'aaa': 'harf1'}, {'bbb': 'harf2'}, {'ccc': 'harf3'}, {'ddd': 'harf4'}]
# print(random.choice(list)) ==== {'ddd': 'harf4'}
# list[0] ==== {'aaa': 'harf1'}

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b  # when b becomes new a
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
