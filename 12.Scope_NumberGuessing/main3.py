i = 50


def foo():
    i = 100
    return i


foo()  # this wont be printed because it only has return value.
# if yu want the function be printed (if yu want that return value to be printed),
# you have to assign it to a value first then print that value.
# new_i = foo()
# print(new_i) gibi...
print(i)


# 50
