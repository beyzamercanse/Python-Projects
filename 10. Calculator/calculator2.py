# CALCULATOR APP new solution


# +
def add(n1, n2):
    return n1+n2

# -


def substract(n1, n2):
    return n1-n2

# *


def multiply(n1, n2):
    return n1*n2

# //


def divide(n1, n2):
    return n1/n2


game_finished = False

while not game_finished:
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))
    symbol = input("enter the operation symbol: ")

    def calculator(num1, symbol, num2):
        if symbol == "+":
            return add(num1, num2)  # return results
        elif symbol == "-":
            return substract(num1, num2)  # return results
        elif symbol == "*":
            return multiply(num1, num2)  # return results
        elif symbol == "/":
            return divide(num1, num2)  # return results
        else:
            print("invalid operation.")

    result = calculator(num1, symbol, num2)
    print(f"{num1} {symbol} {num2} = {result}")

    play_again = input(f"Type 'y' to continue calculating or 'n' to stop: ")
    if play_again == "y":
        game_finished = False
    elif play_again == "n":
        game_finished = True
        print("\n goodbye!")
