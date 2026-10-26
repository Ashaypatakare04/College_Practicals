"""
student.py
Module defining Person (Base Class) and Student (Derived Class).

Syllabus Concepts Covered:
- Object Oriented Programming (OOP): Classes, Objects, Constructors (__init__)
- Inheritance: Student inherits from Person
- Polymorphism & Method Overriding: get_details() and __str__()
- Data Types: Strings, Dictionaries (marks), Tuples (grade scale)
- Functions and conditional control structures
"""

from typing import Dict, Any, Tuple


class Person:
    """
    Base Class representing a generic person.
    Demonstrates OOP encapsulation and inheritance foundation.
    """
    def __init__(self, name: str):
        # Protected attribute
        self._name: str = name

    @property
    def name(self) -> str:
        """Getter for person name."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Setter for person name."""
        self._name = value

    def get_details(self) -> Dict[str, Any]:
        """
        Base method to return person details.
        Demonstrates polymorphism when overridden in child class.
        """
        return {
            "name": self._name
        }

    def __str__(self) -> str:
        return f"Person(name={self._name})"


class Student(Person):
    """
    Derived Class representing a student.
    Inherits from Person base class.
    """

    # Class constant using a Tuple of Tuples for immutable Grade Scale
    # Tuple format: (minimum_percentage_threshold, grade_letter)
    GRADE_SCALE: Tuple[Tuple[float, str], ...] = (
        (90.0, "A+"),
        (80.0, "A"),
        (70.0, "B+"),
        (60.0, "B"),
        (50.0, "C"),
        (40.0, "D"),
        (0.0,  "F"),
    )

    def __init__(self, student_id: str, name: str, class_div: str, marks: Dict[str, float]):
        """
        Constructor (__init__) for Student class.
        Demonstrates super() constructor invocation for inheritance.
        """
        # Call base class constructor
        super().__init__(name)

        self._student_id: str = student_id
        self._class_div: str = class_div
        # Dictionary storing subject name -> mark
        self._marks: Dict[str, float] = marks
        
        # Calculate percentage and grade upon initialization
        self._percentage: float = self.calculate_percentage()
        self._grade: str = self.calculate_grade()

    # --- Properties (Getters and Setters) ---

    @property
    def student_id(self) -> str:
        return self._student_id

    @property
    def class_div(self) -> str:
        return self._class_div

    @class_div.setter
    def class_div(self, value: str):
        self._class_div = value

    @property
    def marks(self) -> Dict[str, float]:
        return self._marks

    @marks.setter
    def marks(self, new_marks: Dict[str, float]):
        self._marks = new_marks
        self._percentage = self.calculate_percentage()
        self._grade = self.calculate_grade()

    @property
    def percentage(self) -> float:
        return self._percentage

    @property
    def grade(self) -> str:
        return self._grade

    # --- Core Business Logic Methods ---

    def calculate_total_marks(self) -> float:
        """
        Calculates the sum of marks across all subjects.
        Uses Python built-in sum() on dictionary values.
        """
        if not self._marks:
            return 0.0
        return round(sum(self._marks.values()), 2)

    def calculate_percentage(self) -> float:
        """
        Calculates percentage based on marks dictionary.
        Assuming each subject is evaluated out of 100 marks.
        """
        if not self._marks:
            return 0.0
        total_obtained = sum(self._marks.values())
        max_possible = len(self._marks) * 100.0
        percent = (total_obtained / max_possible) * 100.0
        return round(percent, 2)

    def calculate_grade(self) -> str:
        """
        Assigns letter grade based on percentage using GRADE_SCALE tuple.
        Demonstrates conditional checks and iteration over tuples.
        
        Grade Range Mapping:
        >= 90% : A+ (Outstanding)
        >= 80% : A  (Excellent)
        >= 70% : B+ (Very Good)
        >= 60% : B  (Good)
        >= 50% : C  (Satisfactory)
        >= 40% : D  (Pass)
        <  40% : F  (Fail)
        """
        pct = self.calculate_percentage()
        for min_score, grade in self.GRADE_SCALE:
            if pct >= min_score:
                return grade
        return "F"

    # --- Polymorphism Demonstration ---

    def get_details(self) -> Dict[str, Any]:
        """
        Method Overriding (Polymorphism):
        Overrides Person.get_details() to provide comprehensive student information.
        """
        # Retrieve base dictionary and extend it
        details = super().get_details()
        details.update({
            "student_id": self._student_id,
            "class_div": self._class_div,
            "marks": self._marks,
            "total_marks": self.calculate_total_marks(),
            "percentage": self._percentage,
            "grade": self._grade
        })
        return details

    def to_dict(self) -> Dict[str, Any]:
        """
        Serializes Student object to dictionary format for JSON storage.
        """
        return {
            "student_id": self._student_id,
            "name": self._name,
            "class_div": self._class_div,
            "marks": self._marks,
            "percentage": self._percentage,
            "grade": self._grade
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Student":
        """
        Factory class method to instantiate a Student object from a dictionary.
        """
        return cls(
            student_id=data.get("student_id", ""),
            name=data.get("name", ""),
            class_div=data.get("class_div", ""),
            marks=data.get("marks", {})
        )

    def __str__(self) -> str:
        """Polymorphic string representation."""
        return (
            f"Student(ID={self._student_id}, Name='{self._name}', "
            f"Class='{self._class_div}', Percentage={self._percentage}%, Grade='{self._grade}')"
        )
