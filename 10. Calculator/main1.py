# fucntion with outputs

def format_name(f_name, l_name):
    format_first = f_name.title()
    format_last = l_name.title()

    return f"{format_first}  {format_last}"  # end of the function


formated = format_name("beyza", "mERCAN")
print(formated)


# if you use return, you have to save the function into a variable like "formated" and print it later  ,,, or print(format_name())
# if you use print instead of return, you just call the function.

# return is the end of the function and nthing after it will be printed.
