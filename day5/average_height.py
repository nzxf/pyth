# student_heights = [180, 124, 165, 173, 189, 169, 146]

# total_height = 0

# for height in student_heights:
#     total_height += height

# average_height = total_height/len(student_heights)

# print(f"The average height of all the students is {average_height}")

# input 180 124 165 173 189 169 146

heights = input("What are the heights of all the students? ")
heights_list = heights.split(" ")

int_heights = []
number_of_students = 0
total = 0

for height in heights_list:
    int_heights.append(int(height))
    number_of_students += 1
    total += height

average = total/number_of_students

print(average)