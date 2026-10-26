"""Input validation and custom exception definitions."""

import re


class ValidationError(Exception):
    """Raised when form input fails validation."""
    pass


class DuplicateIDError(Exception):
    """Raised when student ID already exists."""
    pass


class StudentNotFoundError(Exception):
    """Raised when student record is not found."""
    pass


def validate_student_id(student_id: str) -> str:
    """Validate student ID: 2-15 alphanumeric characters (e.g., TY01, S101)."""
    cleaned_id = student_id.strip()
    if not cleaned_id:
        raise ValidationError("Student ID cannot be empty.")
    if not re.match(r"^[A-Za-z0-9\-_]{2,15}$", cleaned_id):
        raise ValidationError("Invalid Student ID! Must be 2-15 alphanumeric characters.")
    return cleaned_id.upper()


def validate_name(name: str) -> str:
    """Validate student name: only letters, dots, and spaces (2-50 chars)."""
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValidationError("Student Name cannot be empty.")
    if not re.match(r"^[A-Za-z\s.]{2,50}$", cleaned_name):
        raise ValidationError("Invalid Name! Name must contain only alphabets and spaces.")
    return cleaned_name.title()


def validate_class_div(class_div: str) -> str:
    """Validate class/division: 1-15 characters."""
    cleaned_class = class_div.strip()
    if not cleaned_class:
        raise ValidationError("Class / Division cannot be empty.")
    if not re.match(r"^[A-Za-z0-9\s\-_]{1,15}$", cleaned_class):
        raise ValidationError("Invalid Class/Division format.")
    return cleaned_class.upper()


def validate_mark(subject_name: str, mark_value) -> float:
    """Validate subject marks: numeric value between 0 and 100."""
    try:
        val = float(mark_value)
    except (ValueError, TypeError):
        raise ValidationError(f"Marks for '{subject_name}' must be a number.")
    
    if val < 0.0 or val > 100.0:
        raise ValidationError(f"Marks for '{subject_name}' must be between 0 and 100.")
    return round(val, 2)
