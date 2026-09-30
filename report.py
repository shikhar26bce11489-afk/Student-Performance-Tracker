# report.py

from analysis import calculate_performance


def display_report(student):
    result = calculate_performance(student)

    if result is None:
        print("No marks available for this student.")
        return

    print("\n" + "=" * 45)
    print(" STUDENT PERFORMANCE REPORT")
    print("=" * 45)

    print(f"Name : {student['name']}")
    print(f"Roll No. : {student['roll_no']}")

    print("\nSubject Marks:")

    for subject, mark in student["marks"].items():
        print(f"{subject:<15}: {mark:g}")

    print("\nPerformance:")
    print(f"Total : {result['total']:g}/500")
    print(f"Percentage : {result['percentage']:.2f}%")
    print(f"Grade : {result['grade']}")
    print(f"Status : {result['status']}")
    print(f"Highest Marks : {result['highest']}")
    print(f"Lowest Marks : {result['lowest']}")

    print("=" * 45)


def display_all_students(students):
    if not students:
        print("\nNo students available.")
        return

    print("\n--- All Students ---")

    for student in students:
        result = calculate_performance(student)

        if result:
            print(
                f"{student['roll_no']} | "
                f"{student['name']} | "
                f"{result['percentage']:.2f}% | "
                f"Grade: {result['grade']} | "
                f"{result['status']}"
            )
        else:
            print(
                f"{student['roll_no']} | "
                f"{student['name']} | No marks"
            )