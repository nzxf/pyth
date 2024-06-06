import random

random_number = random.randint(1,2)

result = "Your coin got into the manhole."

if random_number == 1:
    result = "head"
else:
    result = "tail"

print(result)