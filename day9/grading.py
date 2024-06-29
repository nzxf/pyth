student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


def score_to_grade (score):
    grade = "Empty!!!"
    if score < 70:
        grade = "Fail"
    elif score <= 80:
        grade = "Accepatable"
    elif score <= 90:
        grade = "Exceeds Expectations"
    elif score > 90:
        grade = "Outstanding"
    return grade


student_grades = {}
for key in student_scores:
    score = student_scores[key]
    student_grades[key] = score_to_grade(score)

print(student_grades)