# Ask current age
age = input("What is your current age? ")

age_as_int = int(age)
max_age = 90

left_year = max_age - age_as_int

left_month = left_year * 12
left_week = left_year * 52
left_day = left_year * 365

message = f"You have {left_day} days, {left_week} weeks, and {left_month} months left."

print(message)
