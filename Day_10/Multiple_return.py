# Functions with outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs..."
    tf_name = f_name.title()
    tl_name = l_name.title()
    return f"{tf_name} {tl_name}"

print(format_name(input("What is your first name?: "), input("What is your last name?: ")))