# Viva Preparation Guide: Student Record Management System
### Course: Advanced Programming Concepts (Python) [231CSEPCC304]
### Class: TY B.Tech CSE (Semester V, NEP Curriculum)

---

## 🎯 Section 1: Object-Oriented Programming (OOP)

### Q1: What Object-Oriented concepts have you implemented in this project?
**Answer:**
We have implemented:
1. **Encapsulation:** Attributes are protected (e.g., `_student_id`, `_name`, `_marks`) and accessed via `@property` getters and setters.
2. **Inheritance:** `Student` class inherits common personal attributes from the `Person` base class.
3. **Polymorphism / Method Overriding:** The `get_details()` method is defined in `Person` and overridden in `Student` to provide extended student-specific information.
4. **Constructors:** Used `__init__()` in both classes, invoking `super().__init__(name)` in the child class.

---

### Q2: Why did you create a `Person` base class when this is a Student Record System?
**Answer:**
In real-world software architecture and academic course standards, creating a `Person` base class demonstrates the concept of **code reusability and inheritance**. A `Person` encapsulates generic human attributes (like name), while `Student` specializes it by adding academic attributes (student ID, class, marks, percentage, grade). If needed in the future, a `Faculty` or `Staff` class could also inherit from `Person`.

---

### Q3: What is the purpose of `super().__init__(name)`?
**Answer:**
`super()` provides access to methods and properties of the parent class (`Person`). Calling `super().__init__(name)` delegates the initialization of the `name` attribute to the parent constructor, preventing code duplication and adhering to the DRY (Don't Repeat Yourself) principle.

---

### Q4: Where is Polymorphism used in your project?
**Answer:**
Polymorphism is demonstrated via **Method Overriding**:
- In `Person`, `get_details()` returns `{"name": self._name}`.
- In `Student`, `get_details()` overrides `Person.get_details()` to add `student_id`, `class_div`, `marks`, `total_marks`, `percentage`, and `grade`.
- In addition, the dunder method `__str__()` is overridden to give polymorphic string representations.

---

## 🎯 Section 2: Data Structures

### Q5: What data structures did you use and why?
**Answer:**
1. **Dictionaries (`dict`):**
   - Used for storing subject marks (e.g., `{"Advanced Python": 88.0, "DBMS": 92.0, "Computer Networks": 85.0}`).
   - Used for in-memory student lookup in `storage.py` where `student_id` acts as the key for $O(1)$ fast lookups.
2. **Tuples (`tuple`):**
   - Used for the immutable `GRADE_SCALE` constant:
     `((90.0, "A+"), (80.0, "A"), (70.0, "B+"), (60.0, "B"), (50.0, "C"), (40.0, "D"), (0.0, "F"))`.
   - Used for column names and heading definitions in the Treeview table.
   - Tuples are preferred here because these configurations must never be modified during runtime.
3. **Lists (`list`):**
   - Used to store sequences of student objects for display, filtering, and JSON serialization.
4. **Sets (`set`):**
   - Used in `get_unique_classes()` method to eliminate duplicates when finding all distinct classes/divisions.

---

### Q6: Where did you use Lambda functions?
**Answer:**
In `storage.py`, lambda functions are used to sort student records:
```python
sorted(student_list, key=lambda s: s.percentage, reverse=True)
```
The lambda function `lambda s: s.percentage` acts as an anonymous inline function that extracts the `percentage` attribute from each student object to sort records without defining a separate named function.

---

## 🎯 Section 3: File Handling & Exception Handling

### Q7: Why did you use JSON for storage instead of SQLite or CSV?
**Answer:**
1. The project requirement strictly mandates standard Python file handling (`open()`, `read()`, `write()`) without requiring external database setups.
2. `JSON` (JavaScript Object Notation) matches Python dictionaries and lists natively (`json.dump` and `json.load`).
3. JSON is human-readable, lightweight, and preserves hierarchical data types (like nested subject mark dictionaries) much better than plain CSV.

---

### Q8: What is the advantage of using `with open(...)`?
**Answer:**
The `with` statement utilizes Python's **context management protocol** (`__enter__` and `__exit__`). It guarantees that the file handle is automatically closed as soon as the block terminates, even if an exception occurs inside the block. This prevents file corruption, memory leaks, and resource locking.

---

### Q9: How do you handle file errors or corrupted files?
**Answer:**
In `storage.py`:
- `FileNotFoundError`: If the JSON file does not exist, the system automatically creates the `data/` directory and generates sample initial records.
- `json.JSONDecodeError`: If the file contains invalid or corrupted JSON, it catches the error, renames the corrupt file to `.bak` for safety, and initializes clean data so the application never crashes.
- `PermissionError` / `IOError`: Handled with informative error alerts.

---

### Q10: What custom exceptions did you create?
**Answer:**
In `validator.py`, we created three custom exceptions inheriting from `Exception`:
1. `ValidationError`: Raised when user input fails format or range checks.
2. `DuplicateIDError`: Raised when attempting to add a student ID that already exists.
3. `StudentNotFoundError`: Raised when attempting to update or delete a non-existent student record.

---

## 🎯 Section 4: Regular Expressions (`re`)

### Q11: How is the `re` module used in your project?
**Answer:**
We use regular expressions in `validator.py` for input validation:
- **Student ID:** `r"^[A-Za-z0-9\-_]{2,15}$"`
  Ensures the ID contains 2 to 15 alphanumeric characters or hyphens/underscores (e.g., `TY01`, `S101`).
- **Student Name:** `r"^[A-Za-z\s.]{2,50}$"`
  Ensures names only contain letters, spaces, and dots (2 to 50 characters), preventing numbers or special characters.
- **Marks:** Checked numerically to ensure values are between `0.0` and `100.0`.

---

## 🎯 Section 5: Tkinter GUI & Event-Driven Architecture

### Q12: What is the difference between `tkinter` and `tkinter.ttk`?
**Answer:**
- Standard `tk` widgets (e.g., `tk.Button`, `tk.Label`) have an older, basic OS look.
- `ttk` (Themed Tkinter) provides modern, native-looking widgets such as `ttk.Treeview`, `ttk.Combobox`, `ttk.Separator`, and supports flexible styling via `ttk.Style()`.

---

### Q13: How does the Treeview table interact with the input form?
**Answer:**
We bind the `<ButtonRelease-1>` event to the Treeview:
```python
self.tree.bind("<ButtonRelease-1>", self.handle_row_selection)
```
When a user clicks on any row in the table, `handle_row_selection` retrieves the selected row's student ID, looks up the student in `storage`, and automatically populates all form fields. This allows one-click editing or updating.

---

### Q14: What is `root.mainloop()`?
**Answer:**
`root.mainloop()` is the Tkinter event loop. It continuously listens for user interactions (mouse clicks, keystrokes, window resizing), keeps the window open, and routes events to their registered callback handlers.

---

### Q15: How is High-DPI screen blurriness avoided on Windows?
**Answer:**
In `main.py`, we call Windows' native DPI awareness API using `ctypes`:
```python
ctypes.windll.shcore.SetProcessDpiAwareness(1)
```
This ensures text and UI elements render crisply on high-resolution displays without blurriness.
