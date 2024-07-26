print("welcome to MY CALCULATOR")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

operator_list = []
for each in operations:
    operator_list.append(each)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input(f"Pick an operation symbol ({",".join(operator_list)}): ")

calculate = operations[operator]
answer = calculate(num1, num2)
print(f"{num1} {operator} {num2} = {answer}")

operator = input("Pick another operator: ")
num3 = int(input("What's the next number?: "))

calculate = operations[operator]
anser = calculate()