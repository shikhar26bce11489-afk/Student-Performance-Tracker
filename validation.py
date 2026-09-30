def find_student(students, roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None