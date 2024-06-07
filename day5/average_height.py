student_heights = [180, 124, 165, 173, 189, 169, 146]

total_height = 0

for height in student_heights:
    total_height += height

average_height = total_height/len(student_heights)

print(f"The average height of all the students is {average_height}")