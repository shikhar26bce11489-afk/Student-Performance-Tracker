def add_student(students):
    print("\n--- Add Student ---")

    roll_no = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()
    branch = input("Enter branch: ").strip()

    student = {
        "roll_no": roll_no,
        "name": name,
        "branch": branch,
        "marks": {}
    }

    students.append(student)
    print("\nStudent added successfully!")
