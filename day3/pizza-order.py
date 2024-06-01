# Greet
print("Welcome to Python Pizza Deliveries!")

# pizza size
size = input("What size pizza do you want? S, M, or L? ")

# pepperoni
add_pepperoni = input("Do you want pepperoni? Y or N? ")

# cheese
extra_cheese = input("Do you want extra cheese? Y or N? ")

# count
bill = 0

if size == "L":
    bill += 25
elif size == "M":
    bill += 20
elif size == "S":
    bill += 15

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")