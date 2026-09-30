# analysis.py

def calculate_performance(student):
    marks = student["marks"]

    if not marks:
        return None

    total = sum(marks.values())
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    status = "PASS" if percentage >= 40 else "FAIL"

    highest_subject = max(marks, key=marks.get)
    lowest_subject = min(marks, key=marks.get)

    return {
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": status,
        "highest": highest_subject,
        "lowest": lowest_subject
    }