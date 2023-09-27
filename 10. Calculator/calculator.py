
# CALCULATOR APP

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
    return n1//n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    # If you add parenthesis after a function it will actually trigger or call a function and you will get the result of the function execution, not the function itself. So we can say that the name of the function is acting like a normal variable.
    "//": divide
}

num1 = int(input("enter the first number:  "))
num2 = int(input("enter the second number:  "))

for symbol in operations:
    print(symbol)

operation_symbol = input("pick an operatiion from the line above:  ")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
