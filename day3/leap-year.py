# Ask year
year = int(input("Which year do you want to check?"))

# On every year that is evenly divisible by 4
is_divisible_by_4 = year / 4
# Except every year that is evenly divisible by 100
is_divisible_by_100 = year / 100
# Unless the year is also evenly divisible by 400
is_divisible_by_400 = year / 400

raw = f"{year}:4={is_divisible_by_4}\n{year}:100={is_divisible_by_100}\n{year}:400={is_divisible_by_400}"

result = "no idea"

# Check
# if (year/4) % 1 == 0.0:
#     if (year/100) % 1 == 0.0:
#         result = "Not Leap Year!"
#         if (year/400) % 1 == 0.0:
#             result = "Leap Year!"
# else:
#     result = "Not Leap Year!"

if year % 4 == 0:
    if year % 100 == 0:
        result = "Not Leap Year!"
        if year % 400 == 0:
            result = "Leap Year!"
else:
    result = "Not Leap Year!"

print(raw)
print(result)