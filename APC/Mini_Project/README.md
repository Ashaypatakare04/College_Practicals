# Student Record Management System

A desktop application built with Python and Tkinter for managing student academic records. Developed as a college mini-project for **Advanced Programming Concepts (Python)**.

---

## Features

- **Add Student:** Register new student records with ID, name, class/division, and subject marks.
- **View Records:** Display student records in an interactive table with vertical and horizontal scrollbars.
- **Search & Filter:** Search students by ID or Name.
- **Update Record:** Select any record to modify details and save changes.
- **Delete Record:** Remove records with a confirmation prompt.
- **Auto Calculation:** Automatically computes percentage and assigns letter grades (A+ to F).
- **Preview Tool:** Preview percentage and grade before saving.
- **Local Persistence:** Saves and loads data automatically from a local JSON file (`data/students.json`).
- **Sort by Performance:** Sort records by percentage in descending order.

---

## Project Structure

```
Mini_Project/
├── main.py              # Application entry point
├── gui.py               # Tkinter GUI layout, Treeview table, and event handlers
├── student.py           # Person (base class) and Student (derived class) models
├── storage.py           # JSON file handling, CRUD operations, and sorting
├── validator.py         # Regex-based input validation and custom exceptions
├── README.md            # Project documentation
└── data/
    └── students.json    # JSON storage file for student records
```

---

## File Overview

| File | Description |
| :--- | :--- |
| `main.py` | Initializes High-DPI display settings and launches the application. |
| `gui.py` | Builds the Tkinter user interface, input forms, and data tables. |
| `student.py` | Contains OOP models (`Person` base class, `Student` child class), inheritance, and grade logic. |
| `storage.py` | Manages reading and writing data to `data/students.json` with error handling. |
| `validator.py` | Validates student IDs, names, and marks using regular expressions. |
| `data/students.json` | Stores student data locally in JSON format. |

---

## How to Run

### Requirements
- Python 3.8+ (Uses only Python Standard Library — no external packages required)

### Run Command
```bash
python main.py
```
