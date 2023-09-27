
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # print("leap year.")
                return True
            else:
                # print("not leap year.")
                return False
        else:
            # ("leap year.")
            return True
    else:
        # print("not leap year.")
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 31, 30, 30, 30]
    if month > 12 and month < 1:
        return "invalid month"
    if is_leap_year(year) and month == 2:
        return 29
    else:
        return month_days[month-1]


year = int(input("enter a year: "))
month = int(input("enter a month number: "))
days = days_in_month(year, month)
print(days)


# example

# def outer_function(a, b):
#     def inner_function(c, d):
#         return c + d
#     return inner_function(a, b)

# result = outer_function(5, 10)
# print(result)

# a = 5, which means c = 5. b = 10, which means d = 10. The output of inner_function becomes the output of outer_function.
