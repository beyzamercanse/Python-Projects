# multiple return values

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return None  # if this executes, the codes below "format_f and format_l and return wont execute, it will just return NONE"
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return f"Result: {format_f_name} {format_l_name}"


print(format_name(input("what is your first name? "),
      input("what is your last name? ")))
