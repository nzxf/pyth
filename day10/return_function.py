# FUNCTION WITH OUTPUT

def format_name(f_name, l_name):
  """Take a first and last name and format it to return the title case version of the name"""
  if f_name == "" or l_name == "":
    return "Please enter a valid input!"
  # f_name = f_name[0].upper() + f_name[1:]
  # l_name = l_name[0].upper() + l_name[1:]
  full_name = f"{f_name} {l_name}"
  # str.title() => turn each first letter of word(s) into capital
  return full_name.title()



print(format_name(input("What is your first name: "), input("What is your last name: ")))