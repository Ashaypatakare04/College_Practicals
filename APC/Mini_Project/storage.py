"""JSON persistence and storage manager for student records."""

import os
import json
from typing import List, Dict, Optional, Set
from student import Student
from validator import DuplicateIDError, StudentNotFoundError


class StudentStorageManager:
    """Manages loading, saving, and querying student records in JSON format."""

    def __init__(self, data_directory: str = "data", filename: str = "students.json"):
        self.data_directory = data_directory
        self.filename = filename
        self.filepath = os.path.join(self.data_directory, self.filename)
        self._students: Dict[str, Student] = {}

        self._ensure_directory_exists()
        self.load_from_file()

    def _ensure_directory_exists(self) -> None:
        """Create data directory if missing."""
        if not os.path.exists(self.data_directory):
            try:
                os.makedirs(self.data_directory, exist_ok=True)
            except OSError as err:
                print(f"[ERROR] Could not create directory '{self.data_directory}': {err}")

    def load_from_file(self) -> None:
        """Load student records from local JSON file."""
        self._students.clear()

        if not os.path.exists(self.filepath):
            self._load_sample_data()
            self.save_to_file()
            return

        try:
            with open(self.filepath, mode="r", encoding="utf-8") as f:
                raw_data = json.load(f)
                if isinstance(raw_data, list):
                    for item in raw_data:
                        try:
                            student = Student.from_dict(item)
                            self._students[student.student_id] = student
                        except Exception:
                            pass
        except (FileNotFoundError, json.JSONDecodeError):
            self._load_sample_data()
            self.save_to_file()
        except IOError as io_err:
            print(f"[ERROR] File read failed: {io_err}")

    def save_to_file(self) -> None:
        """Save all student records to JSON file."""
        self._ensure_directory_exists()
        records_list = [student.to_dict() for student in self._students.values()]

        try:
            with open(self.filepath, mode="w", encoding="utf-8") as f:
                json.dump(records_list, f, indent=4)
        except IOError as io_err:
            raise IOError(f"Failed to save student data: {io_err}")

    def _load_sample_data(self) -> None:
        """Initialize initial sample records."""
        sample_students = [
            Student(
                student_id="TY01",
                name="Aarav Sharma",
                class_div="TY CSE A",
                marks={"Advanced Python": 88.0, "DBMS": 92.0, "Computer Networks": 85.0}
            ),
            Student(
                student_id="TY02",
                name="Diya Kulkarni",
                class_div="TY CSE A",
                marks={"Advanced Python": 95.0, "DBMS": 90.0, "Computer Networks": 94.0}
            ),
            Student(
                student_id="TY03",
                name="Rohan Patil",
                class_div="TY CSE B",
                marks={"Advanced Python": 64.0, "DBMS": 70.0, "Computer Networks": 68.0}
            ),
            Student(
                student_id="TY04",
                name="Sneha Deshmukh",
                class_div="TY CSE B",
                marks={"Advanced Python": 78.0, "DBMS": 82.0, "Computer Networks": 75.0}
            )
        ]
        for s in sample_students:
            self._students[s.student_id] = s

    def add_student(self, student: Student) -> None:
        """Add a new student record."""
        if student.student_id in self._students:
            raise DuplicateIDError(f"Student with ID '{student.student_id}' already exists!")
        self._students[student.student_id] = student
        self.save_to_file()

    def update_student(self, student: Student) -> None:
        """Update an existing student record."""
        if student.student_id not in self._students:
            raise StudentNotFoundError(f"Student ID '{student.student_id}' not found.")
        self._students[student.student_id] = student
        self.save_to_file()

    def delete_student(self, student_id: str) -> Student:
        """Delete student record by ID."""
        if student_id not in self._students:
            raise StudentNotFoundError(f"Student ID '{student_id}' not found.")
        removed = self._students.pop(student_id)
        self.save_to_file()
        return removed

    def get_student(self, student_id: str) -> Optional[Student]:
        """Retrieve student record by ID."""
        return self._students.get(student_id)

    def get_all_students(self) -> List[Student]:
        """Return list of all student objects."""
        return list(self._students.values())

    def search_students(self, query: str) -> List[Student]:
        """Search students by matching ID or Name (case-insensitive)."""
        clean_query = query.strip().lower()
        if not clean_query:
            return self.get_all_students()

        return [
            s for s in self._students.values()
            if clean_query in s.student_id.lower() or clean_query in s.name.lower()
        ]

    def sort_students(self, by: str = "percentage", reverse: bool = True) -> List[Student]:
        """Sort students using a lambda key function."""
        student_list = list(self._students.values())
        if by == "percentage":
            return sorted(student_list, key=lambda s: s.percentage, reverse=reverse)
        elif by == "name":
            return sorted(student_list, key=lambda s: s.name.lower(), reverse=reverse)
        elif by == "id":
            return sorted(student_list, key=lambda s: s.student_id, reverse=reverse)
        return student_list

    def get_unique_classes(self) -> Set[str]:
        """Return set of unique class/division names."""
        return {student.class_div for student in self._students.values()}

    def get_total_count(self) -> int:
        """Return total student count."""
        return len(self._students)
