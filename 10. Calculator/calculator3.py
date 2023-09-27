# CALCULATOR APP new3 solution

from replit import clear
from art import logo
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


def calculator():
    operations = {
        "+": add,
        "-": substract,
        "*": multiply,
        # If you add parenthesis after a function it will actually trigger or call a function and you will get the result of the function execution, not the function itself. So we can say that the name of the function is acting like a normal variable.
        "/": divide
    }

    num1 = int(input("enter a number: "))
    should_continue = True

    while should_continue:
        symbol = input("enter a sumbol (+,-,*,/):   ")
        num2 = int(input("enter the second number:   "))
        # gives us the function we wanna use
        calculation_function = operations[symbol]
        answer = calculation_function(num1, num2)

        print(f" {num1} {operations} {num2} = {answer} ")

        continue_or_not = input(
            "would you like to continue with {answer} then type 'y' if not type 'n': ")
        if continue_or_not == "y":
            num1 = answer  # answer is the new num1
        elif continue_or_not == 'n':
            should_continue = False
            clear()
            # this one if you wanna continue the function (from beginning). if you wanna end it completely, dont type this one.
            calculator()


calculator()
