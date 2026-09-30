# main.py

from data import students
from student import add_student
from marks import enter_marks
from validation import find_student
from report import display_report, display_all_students


def main():
    while True:
        print("\n" + "=" * 45)
        print(" STUDENT PERFORMANCE ANALYZER")
        print("=" * 45)

        print("1. Add Student")
        print("2. Enter / Update Marks")
        print("3. Search Student")
        print("4. View All Students")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            roll_no = input("Enter student roll number: ").strip()

            student = find_student(students, roll_no)

            if student:
                enter_marks(student)
            else:
                print("Student not found.")

        elif choice == "3":
            roll_no = input("Enter student roll number: ").strip()

            student = find_student(students, roll_no)

            if student:
                display_report(student)
            else:
                print("Student not found.")

        elif choice == "4":
            display_all_students(students)

        elif choice == "5":
            print("\nThank you for using Student Performance Analyzer!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()