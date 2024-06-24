import math

# 1 can of paint = 5 square meter of wall
coverage = 5
height = 2
width = 4

def paint_calculator(coverage, height, width):
    area = height * width
    result = area / coverage
    rounded_result = math.ceil(result)
    return f"You'll need {rounded_result} cans of paint"

print(paint_calculator(coverage=5,height=7,width=13))