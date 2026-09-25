Student Performance Analyzer

A Python-based application that analyzes student academic performance by managing student details and marks, calculating results, and generating performance reports.

📌 Project Overview

The Student Performance Analyzer is designed to help students and teachers analyze academic performance in an organized way.

The system allows users to enter student information and marks for different subjects. It then calculates the total marks, percentage, grade, pass/fail status, and identifies the highest- and lowest-scoring subjects.

🎯 Objectives

- Store student details and subject marks.
- Calculate total marks and percentage.
- Automatically assign grades.
- Determine pass/fail status.
- Identify highest and lowest scoring subjects.
- Generate a clear performance report.
- Demonstrate Python programming and problem-solving concepts.

✨ Features

- Add student details
- Enter subject-wise marks
- Validate marks between 0 and 100
- Calculate total marks
- Calculate percentage
- Generate grades
- Determine pass/fail status
- Find highest-scoring subject
- Find lowest-scoring subject
- Search for students
- View student performance reports
- View all students

🛠️ Technologies Used

- Python 3
- Python Functions
- Conditional Statements
- Loops
- Lists
- Dictionaries
- Searching and Sorting
- Exception Handling
- Git & GitHub

📂 Project Structure

Student-Performance-Analyzer/
│
├── main.py
├── student.py
├── marks.py
├── analysis.py
├── report.py
├── validation.py
├── data.py
├── requirements.txt
├── README.md
├── statement.md
│
├── tests/
│   └── test_performance.py
│
└── docs/
    ├── architecture.png
    ├── workflow.png
    ├── use_case.png
    ├── class_diagram.png
    └── sequence_diagram.png

⚙️ Installation

1. Clone the repository

git clone https://github.com/your-username/student-performance-analyzer.git

2. Open the project folder

cd student-performance-analyzer

3. Run the application

python main.py

No external Python libraries are required for the basic version.

▶️ How to Use

After running the program, the main menu will be displayed:

=============================================
       STUDENT PERFORMANCE ANALYZER
=============================================

1. Add Student
2. Search Student
3. View All Students
4. Exit

Select an option by entering the corresponding number.

Example

Enter student name: Rahul
Enter roll number: 101

Enter marks for Mathematics: 85
Enter marks for Physics: 78
Enter marks for Python: 92
Enter marks for English: 81
Enter marks for Chemistry: 74

The system calculates:

Total       : 410/500
Percentage  : 82.00%
Grade       : A
Status      : PASS
Highest     : Python
Lowest      : Chemistry

🧪 Testing

The project includes a testing module to verify important calculations and application functions.

Run the tests using:

python -m unittest discover

Testing includes:

- Total marks calculation
- Percentage calculation
- Grade calculation
- Pass/fail determination
- Highest and lowest subject identification
- Input validation

📊 Project Modules

1. Student Management

Handles student names, roll numbers, and student records.

2. Marks Management

Accepts and validates subject-wise marks.

3. Performance Analysis

Calculates total, percentage, grade, and performance statistics.

4. Report Generation

Creates a structured performance report.

5. Validation

Handles invalid inputs and ensures marks are within the permitted range.

🔄 Workflow

Start
  ↓
Main Menu
  ↓
Add Student
  ↓
Enter Marks
  ↓
Validate Marks
  ↓
Calculate Performance
  ↓
Analyze Results
  ↓
Generate Report
  ↓
Display Results
  ↓
Return to Main Menu / Exit

🔮 Future Enhancements

- Add a graphical user interface (GUI).
- Store data permanently using a database.
- Add charts and graphs for performance analysis.
- Add login and user authentication.
- Export reports to PDF.
- Add semester-wise performance tracking.
- Add class-level performance analytics.

👨‍💻 Author

Student Performance Analyzer

Developed as an academic project to demonstrate Python programming, algorithms, data handling, and problem-solving concepts.

📄 License

This project is created for educational purposes.# Student-Performance-Tracker
