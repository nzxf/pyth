student_scores = input("What are all the student scores? ")

list_of_student_scores = student_scores.split(" ")

int_student_score = []
for score in list_of_student_scores:
    int_student_score.append(int(score))

highest_score = 0
for score in int_student_score:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")

# input: 78 65 89 86 55 91 64 89