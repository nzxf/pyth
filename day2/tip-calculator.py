# Greet user
greeting = "Welcome to the tip calculator"
print(greeting)

# Ask total bill
question1 = "What is the total bill? $"
bill = float(input(question1))

# Ask how many people
question2 = "How many people too split the bill? "
people = int(input(question2))

# Ask tip percentage
question3 = "What percentage tip would you like to give? 10, 12, or 15? "
percentage = float(input(question3))

tip = bill * percentage / 100
total = ( bill + tip ) / people

final_amount = "{:.2f}".format(total)

print("Each person should pay: $" + str(final_amount))