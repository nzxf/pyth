# BMI CALCULATOR 2.0

# Ask height
height = float(input("Enter your height in m: "))
# Ask weight
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / (height ** 2), 1)

if bmi < 18.5:
    result = "underweight"
elif bmi < 25:
    result = "normal weight"
elif bmi < 30:
    result = "overweight"
elif bmi < 35:
    result = "obese"
else:
    result = "clinically obese"

print(f"Your BMI score is {bmi}, you are {result}.")