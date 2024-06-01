print("Welcome to the Love Calculator!")
name1 = input("What is your name?")
name2 = input("what is their name?")

combined_names = name1.lower() + name2.lower()

true = 0
true += combined_names.count("t")
true += combined_names.count("r")
true += combined_names.count("u")
true += combined_names.count("e")
print(true)

love = 0
love += combined_names.count("l")
love += combined_names.count("o")
love += combined_names.count("v")
love += combined_names.count("e")
print(love)

love_score = int(str(true)+str(love))

if love_score < 10 or love_score > 90:
    message = f"Your score is {love_score}, you go together like coke and mentos."
elif love_score >= 40 and love_score <= 50:
    message = f"Your score is {love_score}, you are alright together."
else:
    message = f"Your score is {love_score}"

print(message)