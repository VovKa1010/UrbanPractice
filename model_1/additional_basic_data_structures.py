grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students)
students.sort()

average_score = {}
for student_number in range(0, len(students)):
    student_name = students[student_number]
    student_scores = grades[student_number]

    average_score[student_name] = sum(student_scores) / len(student_scores)

print(average_score)
