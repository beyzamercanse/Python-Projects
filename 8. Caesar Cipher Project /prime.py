
# QUESTION 1: check if prime
n = int(input("enter a number: "))


def prime_checker(n):

    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            print(f"{n} can be divided by {i}.")

    if is_prime == True:
        print(f"{n} is a prime number. ")
    else:
        print(f"{n} is not a prime number. ")


prime_checker(n)
