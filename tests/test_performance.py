from analysis import calculate_performance


def test_performance_calculation():
    student = {
        "roll_no": "101",
        "name": "Test Student",
        "branch": "CSE",
        "marks": {
            "Mathematics": 80,
            "Physics": 75,
            "Python": 90,
            "English": 85,
            "Chemistry": 70
        }
    }

    result = calculate_performance(student)

    assert result["total"] == 400
    assert result["percentage"] == 80
    assert result["grade"] == "A"
    assert result["status"] == "PASS"