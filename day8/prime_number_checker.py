# Prime Number = number only divisible by one and itself

n = int(input("Enter a number: "))


def prime_checker(number=n):
    numbers = []
    for each in range(1, number + 1):
        if number % each == 0:
            numbers.append(each)
            # print(f"{number} % {each}")
    # print(numbers)

    if len(numbers) == 2  :
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

prime_checker(n)