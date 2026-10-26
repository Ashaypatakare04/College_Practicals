"""
test_system.py
Unit and integration test script for Student Record Management System.
Verifies all 10 core requirements and syllabus features without launching the GUI.
"""

import os
import shutil
from student import Person, Student
from storage import StudentStorageManager
from validator import (
    validate_student_id,
    validate_name,
    validate_class_div,
    validate_mark,
    ValidationError,
    DuplicateIDError,
    StudentNotFoundError,
)


def run_tests():
    print("==================================================")
    print("RUNNING SYLLABUS & FEATURE VERIFICATION TESTS")
    print("==================================================")

    # 1. Test OOP: Inheritance and Polymorphism
    print("[TEST 1] Testing OOP (Person base class, Student child class, Polymorphism)...")
    person = Person("Test Person")
    student = Student("T101", "Aarav Sharma", "TY CSE A", {"Advanced Python": 95, "DBMS": 90, "Computer Networks": 88})
    
    assert isinstance(student, Person), "Student should inherit from Person!"
    assert student.name == "Aarav Sharma"
    assert student.student_id == "T101"
    
    # Polymorphism: get_details() should return different keys
    person_details = person.get_details()
    student_details = student.get_details()
    assert "student_id" not in person_details
    assert "student_id" in student_details
    print("  -> Passed: Inheritance and Polymorphism verified.")

    # 2. Test Percentage & Grade Calculation
    print("[TEST 2] Testing Percentage and Grade Calculations...")
    # 95 + 90 + 88 = 273 / 3 = 91.0 % -> Grade A+
    assert student.calculate_total_marks() == 273.0
    assert student.percentage == 91.0
    assert student.grade == "A+"

    # Test boundary grade values
    s_bplus = Student("T102", "Diya", "TY CSE A", {"Sub1": 75, "Sub2": 72, "Sub3": 78})
    assert s_bplus.percentage == 75.0
    assert s_bplus.grade == "B+"

    s_fail = Student("T103", "Fail Case", "TY CSE A", {"Sub1": 30, "Sub2": 35, "Sub3": 38})
    assert s_fail.percentage == 34.33
    assert s_fail.grade == "F"
    print("  -> Passed: Percentage and Grade logic correct.")

    # 3. Test Regex Validation
    print("[TEST 3] Testing Regular Expressions input validation...")
    # Valid
    assert validate_student_id("TY01") == "TY01"
    assert validate_name("Aarav Sharma") == "Aarav Sharma"
    assert validate_class_div("TY CSE-A") == "TY CSE-A"
    assert validate_mark("Python", 85) == 85.0

    # Invalid student ID
    try:
        validate_student_id("!!Invalid##")
        assert False, "Should have raised ValidationError for invalid ID"
    except ValidationError:
        pass

    # Invalid student Name (numbers in name)
    try:
        validate_name("John123")
        assert False, "Should have raised ValidationError for numbers in name"
    except ValidationError:
        pass

    # Invalid marks (< 0 or > 100)
    try:
        validate_mark("DBMS", 105)
        assert False, "Should have raised ValidationError for marks > 100"
    except ValidationError:
        pass
    print("  -> Passed: Regex and input validations work as expected.")

    # 4. Test Storage & File Handling (JSON Persistence)
    print("[TEST 4] Testing Storage Manager (JSON persistence, CRUD)...")
    test_dir = "test_data"
    test_file = "test_students.json"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)

    manager = StudentStorageManager(data_directory=test_dir, filename=test_file)
    assert os.path.exists(os.path.join(test_dir, test_file)), "Storage file should be created automatically!"

    # Add student
    manager.add_student(student)
    assert manager.get_student("T101") is not None
    assert manager.get_student("T101").name == "Aarav Sharma"

    # Duplicate check
    try:
        manager.add_student(student)
        assert False, "Should raise DuplicateIDError"
    except DuplicateIDError:
        pass

    # Update student
    updated = Student("T101", "Aarav Sharma Updated", "TY CSE B", {"Advanced Python": 98, "DBMS": 92, "Computer Networks": 95})
    manager.update_student(updated)
    assert manager.get_student("T101").name == "Aarav Sharma Updated"
    assert manager.get_student("T101").class_div == "TY CSE B"

    # Search student
    search_res = manager.search_students("Updated")
    assert len(search_res) == 1 and search_res[0].student_id == "T101"

    # Sorting with lambda
    top_students = manager.sort_students(by="percentage", reverse=True)
    assert len(top_students) >= 1

    # Delete student
    deleted = manager.delete_student("T101")
    assert deleted.student_id == "T101"
    assert manager.get_student("T101") is None

    # Test Reloading from Disk
    manager2 = StudentStorageManager(data_directory=test_dir, filename=test_file)
    assert manager2.get_student("T101") is None

    # Clean up test data
    shutil.rmtree(test_dir)
    print("  -> Passed: File handling and persistence verified.")

    print("==================================================")
    print("ALL TESTS PASSED SUCCESSFULLY! (100% COMPLIANT)")
    print("==================================================")


if __name__ == "__main__":
    run_tests()
