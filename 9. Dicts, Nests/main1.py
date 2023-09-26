student_scores = {"Harry": 81, "Ron": 78,
                  "Hermione": 99, "Draco": 74, "Neville": 62}

# create empty dict called student_grades
student_grades = {}

# add grades to student_grades
for student in student_scores:  # this prints the key only,  not the value
    score = student_scores[student]
    if score > 90:
        student_grades[student] = " outstanding"
    elif score > 80:
        student_grades[student] = " exceeds expectation"
    elif score > 70:
        student_grades[student] = "acceptable"
    else:
        student_grades[student] = " FAIL "

print(student_grades)
