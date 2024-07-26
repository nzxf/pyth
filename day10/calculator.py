logo = ''' __________
| ________ |
||12345678||
|""""""""""|
|[M|#|C][-]|
|[7|8|9][+]|
|[4|5|6][x]|
|[1|2|3][%]|
|[.|O|:][=]|
"----------" '''

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


def calculator():
    should_continue = True

    print(logo)
    num1 = float(input("Enter the first number: "))

    while should_continue:
        operator = input(f"Pick an operation symbol ({",".join(operator_list)}): ")
        num2 = float(input("Enter the second number: "))

        calculate = operations[operator]
        answer = calculate(num1, num2)
        
        print(f"{num1} {operator} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            # RECURSION
            calculator()

calculator()

# def calculate(op, num1, num2):
#     if op == "+":
#         return num1 + num2
#     if op == "-":
#         return num1 - num2
#     if op == "*":
#         return num1 * num2
#     if op == "/":
#         return num1 / num2
    

# finished = False
# keep_going = "n"
# current_result = 1
# while not finished:
#     if keep_going == "n":
#         first_num = int(input("Enter the first number: "))
#     if keep_going == "y":
#         first_num = current_result
#     operator = input("Pick an operation (+, -, *, or /): ")
#     second_num = int(input("Enter the second number: "))

#     result = calculate(operator, first_num, second_num)
#     current_result = result
#     print(result)
    
#     keep_going = input("Type 'y' to continue and 'n' to start new: ")