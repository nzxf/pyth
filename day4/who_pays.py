import random

names = input("Who is participating in this games of Brunch Russian Roullete? Give me everybody's names, separated by comma. ")

name_list = names.split(", ")

random_number = random.randint(0, len(name_list)-1)
print(f"The lucky one who's gonna pay is {name_list[random_number]}")

random_name = random.choice(name_list)
print(f"The lucky one who's gonna pay is {random_name}")