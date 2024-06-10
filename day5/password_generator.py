import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
all_types = [letters, numbers, symbols]

print("Welcome to PyPassword Generator!")
num_of_letter = int(input("How many letters would you like in your password? "))
num_of_number = int(input("How many numbers would you like in you password? "))
num_of_symbol = int(input("How many symbols would you like in you password? "))

# total = num_of_letter + num_of_number + num_of_symbol
# list_of_letter = []
# list_of_number = []
# list_of_symbol = []

# FULLY MANUAL
# chosen_char = []
# for num in range(0, num_of_letter):
#     chosen_char.insert(random.randint(0, num), letters[random.randint(0, len(letters) - 1)])
# for num in range(0, num_of_number):
#     chosen_char.insert(random.randint(0, len(chosen_char)), str(numbers[random.randint(0, len(numbers) - 1)]))
# for num in range(0, num_of_symbol):
#     chosen_char.insert(random.randint(0, len(chosen_char)), symbols[random.randint(0, len(symbols) - 1)])
# password = "".join(chosen_char)

# ALMOST MANUAL
# chosen_char = []
# for num in range(0, num_of_letter):
#     chosen_char.insert(random.randint(0, num), random.choice(letters))
# for num in range(0, num_of_number):
#     chosen_char.insert(random.randint(0, len(chosen_char)), str(random.choice(numbers)))
# for num in range(0, num_of_symbol):
#     chosen_char.insert(random.randint(0, len(chosen_char)), random.choice(symbols))
# password = "".join(chosen_char)


chosen_char = []
for num in range(0, num_of_letter):
    chosen_char.append(random.choice(letters))
for num in range(0, num_of_number):
    chosen_char.append(str(random.choice(numbers)))
for num in range(0, num_of_symbol):
    chosen_char.append(random.choice(symbols))

random.shuffle(chosen_char)
password = "".join(chosen_char)

print(f"Your secured password: {password}")