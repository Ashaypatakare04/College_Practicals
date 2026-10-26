"""
validator.py
Module for input validation using Regular Expressions (re)
and custom exception definitions.

Syllabus Concepts Covered:
- Regular Expressions (re module)
- Exception Handling (Custom Exceptions, try-except)
- Functions and conditional statements
"""

import re


class ValidationError(Exception):
    """Custom exception raised when form inputs fail validation rules."""
    pass


class DuplicateIDError(Exception):
    """Custom exception raised when attempting to add a student with an existing ID."""
    pass


class StudentNotFoundError(Exception):
    """Custom exception raised when a requested student ID is not found."""
    pass


def validate_student_id(student_id: str) -> str:
    """
    Validates Student ID using Regular Expression.
    Rule: Must be 2-15 alphanumeric characters (hyphens and underscores allowed).
    Example valid: S101, TYCSE-01, 23101
    """
    cleaned_id = student_id.strip()
    if not cleaned_id:
        raise ValidationError("Student ID cannot be empty.")
    
    # Regular expression pattern: letters, numbers, hyphens, underscores (length 2-15)
    id_pattern = r"^[A-Za-z0-9\-_]{2,15}$"
    if not re.match(id_pattern, cleaned_id):
        raise ValidationError(
            "Invalid Student ID! Must be 2-15 alphanumeric characters (e.g., S101, TY01)."
        )
    return cleaned_id.upper()


def validate_name(name: str) -> str:
    """
    Validates Student Name using Regular Expression.
    Rule: Must contain only alphabets, spaces, and dots; length 2 to 50 characters.
    Example valid: Ashay Patakare, John Doe, R. Sharma
    """
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValidationError("Student Name cannot be empty.")
    
    # Regular expression pattern: only letters, dots, and spaces (length 2-50)
    name_pattern = r"^[A-Za-z\s.]{2,50}$"
    if not re.match(name_pattern, cleaned_name):
        raise ValidationError(
            "Invalid Name! Name should only contain alphabets and spaces (2-50 characters)."
        )
    return cleaned_name.title()


def validate_class_div(class_div: str) -> str:
    """
    Validates Class/Division string.
    Rule: Must be 1 to 15 alphanumeric characters with spaces or hyphens.
    Example valid: TY CSE, TY-A, B.Tech Div 1
    """
    cleaned_class = class_div.strip()
    if not cleaned_class:
        raise ValidationError("Class / Division cannot be empty.")
    
    class_pattern = r"^[A-Za-z0-9\s\-_]{1,15}$"
    if not re.match(class_pattern, cleaned_class):
        raise ValidationError(
            "Invalid Class/Division! Allowed characters: letters, numbers, spaces, '-' (1-15 chars)."
        )
    return cleaned_class.upper()


def validate_mark(subject_name: str, mark_value) -> float:
    """
    Validates a single subject mark.
    Rule: Must be a numeric value between 0.0 and 100.0.
    """
    # Convert string to float if needed
    try:
        val = float(mark_value)
    except (ValueError, TypeError):
        raise ValidationError(
            f"Marks for '{subject_name}' must be a valid number between 0 and 100."
        )
    
    if val < 0.0 or val > 100.0:
        raise ValidationError(
            f"Marks for '{subject_name}' must be between 0 and 100. Received: {val}"
        )
    
    return round(val, 2)
