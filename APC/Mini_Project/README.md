# Student Record Management System

A desktop application developed using **Python** and **Tkinter** for the college mini-project requirement of **Advanced Programming Concepts (Python)**, Course Code: **231CSEPCC304** (TY CSE Semester V, NEP Curriculum).

---

## 📌 Project Overview

The **Student Record Management System** is a standalone, lightweight, and robust desktop application designed to manage student academic records. It allows teachers and administrators to add, view, search, update, and delete student records, while automatically calculating total marks, percentage, and letter grades.

All student data is persisted locally in a structured `JSON` file using standard Python file handling—avoiding any complex external database or heavy third-party framework while remaining strictly aligned with the prescribed syllabus.

---

## 🎯 Syllabus Mapping (Course Code: 231CSEPCC304)

This project strictly follows the **Advanced Programming Concepts** syllabus without introducing unnecessary external dependencies.

| Syllabus Concept | Implementation in Code | File Reference |
| :--- | :--- | :--- |
| **Python Basics & Variables** | Variables, type hinting, arithmetic, relational & logical operators | All files |
| **Data Types & Data Structures** | Strings (names, IDs), Dictionaries (subject marks, student objects), Lists (table rows, student records), Tuples (immutable grade scale, table columns), Sets (unique classes/divisions) | `student.py`, `storage.py`, `gui.py` |
| **Functions & Lambda Expressions** | Modular functions, `lambda s: s.percentage` used in record sorting | `storage.py`, `validator.py`, `gui.py` |
| **OOP: Classes & Objects** | Encapsulated classes, object instantiation, getters and setters | `student.py`, `storage.py`, `gui.py` |
| **OOP: Inheritance** | `Student` class inherits from `Person` base class using `super().__init__()` | `student.py` |
| **OOP: Polymorphism** | Method overriding in `get_details()` and `__str__()` methods | `student.py` |
| **File Handling & Directories** | `with open(...)`, `json.dump()`, `json.load()`, `os.path`, `os.makedirs()` | `storage.py` |
| **Exception Handling** | `try-except-finally`, custom exceptions (`ValidationError`, `DuplicateIDError`, `StudentNotFoundError`), handling `FileNotFoundError`, `JSONDecodeError` | `validator.py`, `storage.py`, `gui.py` |
| **Tkinter GUI** | `tk.Tk`, `ttk.Treeview`, `ttk.Frame`, `ttk.Label`, `ttk.Entry`, `ttk.Button`, `ttk.Scrollbar`, `messagebox` | `gui.py`, `main.py` |
| **Regular Expressions (`re`)** | Regex patterns for validating student ID (`^[A-Za-z0-9\-_]{2,15}$`) and Name (`^[A-Za-z\s.]{2,50}$`) | `validator.py` |

---

## 🚀 Key Features

1. **Add Student**: Enter Student ID, Full Name, Class/Division, and subject marks (Advanced Python, DBMS, Computer Networks).
2. **View Students**: Interactive `ttk.Treeview` table displaying all student records with vertical and horizontal scrollbars.
3. **Search Student**: Fast real-time search by Student ID or Name.
4. **Update Student**: Single-click a table row to populate the form, edit details, and save changes.
5. **Delete Student**: Delete student records with a confirmation dialog box (`messagebox.askyesno`).
6. **Calculate Percentage**: Calculates percentage based on total marks obtained across subjects.
7. **Calculate Grade**: Automatically assigns letter grades (`A+`, `A`, `B+`, `B`, `C`, `D`, `F`) based on marks ranges.
8. **Live Preview**: "🧮 Preview % & Grade" button lets you preview results before saving.
9. **Persistent JSON Storage**: Records are automatically stored in `data/students.json` with error recovery.
10. **Auto-Load on Startup**: Pre-loads saved records upon application startup.
11. **Clear Form**: One-click reset to clear all input fields.
12. **Top Performers (Sort %)**: One-click sorting of students by percentage in descending order using Python lambda functions.

---

## 📊 Grading Criteria (NEP Standard)

| Percentage Range | Letter Grade | Description |
| :---: | :---: | :---: |
| **≥ 90.0%** | **A+** | Outstanding |
| **≥ 80.0% and < 90.0%** | **A** | Excellent |
| **≥ 70.0% and < 80.0%** | **B+** | Very Good |
| **≥ 60.0% and < 70.0%** | **B** | Good |
| **≥ 50.0% and < 60.0%** | **C** | Satisfactory |
| **≥ 40.0% and < 50.0%** | **D** | Pass |
| **< 40.0%** | **F** | Fail |

---

## 📂 Project Structure

```
Python_mini_project/
│
├── main.py              # Application entry point with Windows High-DPI support
├── student.py           # OOP Models: Person (Base), Student (Child), Polymorphism
├── storage.py           # File handling, JSON persistence, CRUD, sorting with lambda
├── validator.py         # Regular expressions (re) and custom exceptions
├── gui.py               # Tkinter desktop GUI (ttk widgets, Treeview, Event binding)
├── test_system.py       # Automated syllabus & integration test suite
├── README.md            # Project documentation and syllabus mapping
├── VIVA_QUESTIONS.md    # Comprehensive Viva preparation guide with Q&A
└── data/
    └── students.json    # JSON storage containing persisted records
```

---

## 🛠️ How to Run the Application

### Prerequisites
- Python 3.8 or higher (tested on Python 3.13)
- No external `pip install` required! The project uses only Python's standard library.

### Execution
Open your terminal or command prompt in the project directory and run:

```bash
python main.py
```

### Running the Test Suite
To verify all OOP features, regex validation, and storage operations without launching the GUI:

```bash
python test_system.py
```

---

## 🎓 College Lab Viva Highlights

- **Base Class & Inheritance:** `Student` derives from `Person` via `class Student(Person):` and invokes `super().__init__(name)`.
- **Polymorphism:** `get_details()` method is overridden in `Student` to provide extended academic details.
- **Tuples:** `GRADE_SCALE` is defined as a tuple of tuples `((90.0, "A+"), ...)` because grading thresholds are immutable constants.
- **Dictionaries:** Marks are structured as key-value pairs `{"Advanced Python": 88.0, "DBMS": 92.0, "Computer Networks": 85.0}`.
- **Lambda Function:** `sorted(student_list, key=lambda s: s.percentage, reverse=True)` sorts students cleanly.
- **Regular Expressions:** `re.match()` prevents numbers in names and invalid characters in student IDs.
