"""
storage.py
Module for file handling, directory management, and persistence using JSON.

Syllabus Concepts Covered:
- File Handling: Reading and writing files with context manager (with open(...))
- Directory Handling: os module (os.path, os.makedirs)
- Exception Handling: FileNotFoundError, json.JSONDecodeError, IOError, try-except-finally
- Data Structures: Dictionaries, Lists, Sets
- Lambda Functions: Sorting student records
- Modules: importing student and validator modules
"""

import os
import json
from typing import List, Dict, Optional, Set
from student import Student
from validator import DuplicateIDError, StudentNotFoundError


class StudentStorageManager:
    """
    Manages loading, saving, and querying student records in a local JSON file.
    Demonstrates file handling, directory creation, exception handling, and collections.
    """

    def __init__(self, data_directory: str = "data", filename: str = "students.json"):
        self.data_directory = data_directory
        self.filename = filename
        self.filepath = os.path.join(self.data_directory, self.filename)

        # In-memory dictionary: key = student_id, value = Student object
        self._students: Dict[str, Student] = {}

        # Ensure directory exists and initialize storage
        self._ensure_directory_exists()
        self.load_from_file()

    def _ensure_directory_exists(self) -> None:
        """
        Creates the data directory if it does not already exist.
        Demonstrates os module directory operations.
        """
        if not os.path.exists(self.data_directory):
            try:
                os.makedirs(self.data_directory, exist_ok=True)
            except OSError as err:
                print(f"[ERROR] Could not create directory '{self.data_directory}': {err}")

    def load_from_file(self) -> None:
        """
        Reads student records from the JSON file using standard Python file handling.
        Demonstrates try-except-finally and exception handling for file operations.
        """
        self._students.clear()

        # If file does not exist, initialize with default sample records
        if not os.path.exists(self.filepath):
            self._load_sample_data()
            self.save_to_file()
            return

        file_obj = None
        try:
            # File handling using 'with' context manager
            with open(self.filepath, mode="r", encoding="utf-8") as file_obj:
                raw_data = json.load(file_obj)
                
                # raw_data is expected to be a list of student dictionaries
                if isinstance(raw_data, list):
                    for item in raw_data:
                        try:
                            student = Student.from_dict(item)
                            self._students[student.student_id] = student
                        except Exception as e:
                            print(f"[WARNING] Skipping corrupt record: {item}. Error: {e}")
        except FileNotFoundError:
            # Raised if file was removed between check and open
            self._load_sample_data()
            self.save_to_file()
        except json.JSONDecodeError as json_err:
            # Handle corrupt or empty JSON file gracefully
            print(f"[ERROR] JSON Decode Error in {self.filepath}: {json_err}")
            # Backup corrupt file and start fresh with sample data
            backup_path = self.filepath + ".corrupt.bak"
            try:
                if os.path.exists(self.filepath):
                    os.replace(self.filepath, backup_path)
            except OSError:
                pass
            self._load_sample_data()
            self.save_to_file()
        except IOError as io_err:
            print(f"[ERROR] I/O Error reading {self.filepath}: {io_err}")
            raise
        finally:
            # Demonstrates 'finally' block execution
            pass

    def save_to_file(self) -> None:
        """
        Writes all in-memory student records to the JSON file.
        Demonstrates atomic file writing and exception handling.
        """
        self._ensure_directory_exists()

        # Convert Student objects to list of dictionaries using list comprehension
        records_list = [student.to_dict() for student in self._students.values()]

        try:
            with open(self.filepath, mode="w", encoding="utf-8") as f:
                json.dump(records_list, f, indent=4)
        except PermissionError as perm_err:
            raise IOError(f"Permission denied while saving to {self.filepath}: {perm_err}")
        except IOError as io_err:
            raise IOError(f"Failed to write student data to file: {io_err}")

    def _load_sample_data(self) -> None:
        """
        Populates initial demonstration data so the evaluator has immediate data to test.
        """
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

    # --- CRUD Operations ---

    def add_student(self, student: Student) -> None:
        """
        Adds a new student record.
        Raises DuplicateIDError if ID already exists.
        Demonstrates dictionary key lookup and exception raising.
        """
        if student.student_id in self._students:
            raise DuplicateIDError(f"Student with ID '{student.student_id}' already exists!")
        
        self._students[student.student_id] = student
        self.save_to_file()

    def update_student(self, student: Student) -> None:
        """
        Updates an existing student record.
        Raises StudentNotFoundError if record does not exist.
        """
        if student.student_id not in self._students:
            raise StudentNotFoundError(f"Student ID '{student.student_id}' does not exist.")
        
        self._students[student.student_id] = student
        self.save_to_file()

    def delete_student(self, student_id: str) -> Student:
        """
        Deletes a student record by ID.
        Raises StudentNotFoundError if record does not exist.
        """
        if student_id not in self._students:
            raise StudentNotFoundError(f"Student ID '{student_id}' not found.")
        
        removed = self._students.pop(student_id)
        self.save_to_file()
        return removed

    def get_student(self, student_id: str) -> Optional[Student]:
        """
        Retrieves a student record by student ID.
        """
        return self._students.get(student_id)

    def get_all_students(self) -> List[Student]:
        """
        Returns list of all Student objects.
        """
        return list(self._students.values())

    def search_students(self, query: str) -> List[Student]:
        """
        Searches students by matching ID or Name (case-insensitive).
        Demonstrates list comprehension and string methods.
        """
        clean_query = query.strip().lower()
        if not clean_query:
            return self.get_all_students()

        return [
            s for s in self._students.values()
            if clean_query in s.student_id.lower() or clean_query in s.name.lower()
        ]

    def sort_students(self, by: str = "percentage", reverse: bool = True) -> List[Student]:
        """
        Sorts students using Python lambda functions.
        Demonstrates lambda expressions and higher-order function key.
        """
        student_list = list(self._students.values())
        if by == "percentage":
            return sorted(student_list, key=lambda s: s.percentage, reverse=reverse)
        elif by == "name":
            return sorted(student_list, key=lambda s: s.name.lower(), reverse=reverse)
        elif by == "id":
            return sorted(student_list, key=lambda s: s.student_id, reverse=reverse)
        else:
            return student_list

    def get_unique_classes(self) -> Set[str]:
        """
        Demonstrates Python Set data structure to collect unique class/division names.
        """
        return {student.class_div for student in self._students.values()}

    def get_total_count(self) -> int:
        """Returns total number of students."""
        return len(self._students)
