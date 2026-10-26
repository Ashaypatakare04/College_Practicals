"""Student and Person class models with OOP inheritance and polymorphism."""

from typing import Dict, Any, Tuple


class Person:
    """Base class representing a person."""

    def __init__(self, name: str):
        self._name: str = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    def get_details(self) -> Dict[str, Any]:
        """Return basic person details."""
        return {"name": self._name}

    def __str__(self) -> str:
        return f"Person(name={self._name})"


class Student(Person):
    """Student class inheriting from Person."""

    # Grade thresholds: (minimum_percentage, grade)
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
        super().__init__(name)
        self._student_id: str = student_id
        self._class_div: str = class_div
        self._marks: Dict[str, float] = marks
        self._percentage: float = self.calculate_percentage()
        self._grade: str = self.calculate_grade()

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

    def calculate_total_marks(self) -> float:
        """Calculate total marks across all subjects."""
        return round(sum(self._marks.values()), 2) if self._marks else 0.0

    def calculate_percentage(self) -> float:
        """Calculate percentage assuming 100 marks per subject."""
        if not self._marks:
            return 0.0
        return round((sum(self._marks.values()) / (len(self._marks) * 100.0)) * 100.0, 2)

    def calculate_grade(self) -> str:
        """Assign letter grade based on percentage."""
        pct = self.calculate_percentage()
        for min_score, grade in self.GRADE_SCALE:
            if pct >= min_score:
                return grade
        return "F"

    def get_details(self) -> Dict[str, Any]:
        """Override Person.get_details() to include academic data."""
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
        """Serialize student data to dictionary for JSON storage."""
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
        """Instantiate Student from dictionary."""
        return cls(
            student_id=data.get("student_id", ""),
            name=data.get("name", ""),
            class_div=data.get("class_div", ""),
            marks=data.get("marks", {})
        )

    def __str__(self) -> str:
        return f"Student(ID={self._student_id}, Name='{self._name}', Grade='{self._grade}')"
