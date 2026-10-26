"""Tkinter GUI interface for Student Record Management System."""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, Optional

from student import Student
from storage import StudentStorageManager
from validator import (
    ValidationError,
    DuplicateIDError,
    StudentNotFoundError,
    validate_student_id,
    validate_name,
    validate_class_div,
    validate_mark,
)


class StudentManagementApp:
    """Main GUI application class."""

    SUBJECTS = ("Advanced Python", "DBMS", "Computer Networks")

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Student Record Management System | TY CSE")
        self.root.geometry("1100x680")
        self.root.minsize(980, 600)
        self.root.configure(bg="#F1F5F9")

        self.storage = StudentStorageManager()
        self.selected_student_id: Optional[str] = None

        self._configure_styles()
        self._create_header()
        self._create_main_content()
        self._create_status_bar()

        self.refresh_table()

    def _configure_styles(self) -> None:
        """Configure ttk styles."""
        style = ttk.Style()
        style.theme_use("clam")

        bg_card = "#FFFFFF"
        style.configure("Card.TFrame", background=bg_card, relief="flat")
        style.configure("TLabel", background=bg_card, font=("Segoe UI", 10))
        style.configure("Header.TLabel", font=("Segoe UI", 11, "bold"), foreground="#1E293B", background=bg_card)
        style.configure("SubHeader.TLabel", font=("Segoe UI", 9), foreground="#64748B", background=bg_card)
        style.configure("TButton", font=("Segoe UI", 9, "bold"), padding=6)
        style.configure(
            "Treeview",
            background="#FFFFFF",
            foreground="#1E293B",
            rowheight=26,
            fieldbackground="#FFFFFF",
            font=("Segoe UI", 9)
        )
        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 9, "bold"),
            background="#E2E8F0",
            foreground="#0F172A",
            padding=5
        )
        style.map("Treeview", background=[("selected", "#3B82F6")], foreground=[("selected", "#FFFFFF")])

    def _create_header(self) -> None:
        """Create top title banner."""
        header_frame = tk.Frame(self.root, bg="#1E3A8A", height=70)
        header_frame.pack(fill="x", side="top")

        title_label = tk.Label(
            header_frame,
            text="🎓 Student Record Management System",
            font=("Segoe UI", 16, "bold"),
            bg="#1E3A8A",
            fg="#FFFFFF"
        )
        title_label.pack(side="left", padx=20, pady=12)

        subtitle_label = tk.Label(
            header_frame,
            text="Course: 231CSEPCC304 (Advanced Python) | TY CSE",
            font=("Segoe UI", 10),
            bg="#1E3A8A",
            fg="#BFDBFE"
        )
        subtitle_label.pack(side="right", padx=20, pady=16)

    def _create_main_content(self) -> None:
        """Create left form and right table panels."""
        content = tk.Frame(self.root, bg="#F1F5F9")
        content.pack(fill="both", expand=True, padx=15, pady=12)

        self.left_frame = tk.Frame(content, bg="#FFFFFF", padx=18, pady=15, relief="solid", bd=1)
        self.left_frame.pack(side="left", fill="y", padx=(0, 10))

        self.right_frame = tk.Frame(content, bg="#F1F5F9")
        self.right_frame.pack(side="right", fill="both", expand=True)

        self._build_form_inputs()
        self._build_search_and_table()

    def _build_form_inputs(self) -> None:
        """Build input form fields and action buttons."""
        lbl_form_title = tk.Label(
            self.left_frame,
            text="Student Details Form",
            font=("Segoe UI", 12, "bold"),
            bg="#FFFFFF",
            fg="#1E3A8A"
        )
        lbl_form_title.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 12))

        self.var_id = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_class = tk.StringVar()
        self.var_mark_python = tk.StringVar()
        self.var_mark_dbms = tk.StringVar()
        self.var_mark_cn = tk.StringVar()
        self.var_percentage = tk.StringVar(value="-- %")
        self.var_grade = tk.StringVar(value="--")

        # Student ID
        tk.Label(self.left_frame, text="Student ID *", bg="#FFFFFF", font=("Segoe UI", 9, "bold")).grid(
            row=1, column=0, sticky="w", pady=4
        )
        self.entry_id = ttk.Entry(self.left_frame, textvariable=self.var_id, width=24, font=("Segoe UI", 9))
        self.entry_id.grid(row=1, column=1, sticky="ew", pady=4, padx=(8, 0))

        # Student Name
        tk.Label(self.left_frame, text="Full Name *", bg="#FFFFFF", font=("Segoe UI", 9, "bold")).grid(
            row=2, column=0, sticky="w", pady=4
        )
        self.entry_name = ttk.Entry(self.left_frame, textvariable=self.var_name, width=24, font=("Segoe UI", 9))
        self.entry_name.grid(row=2, column=1, sticky="ew", pady=4, padx=(8, 0))

        # Class / Division
        tk.Label(self.left_frame, text="Class / Div *", bg="#FFFFFF", font=("Segoe UI", 9, "bold")).grid(
            row=3, column=0, sticky="w", pady=4
        )
        self.entry_class = ttk.Entry(self.left_frame, textvariable=self.var_class, width=24, font=("Segoe UI", 9))
        self.entry_class.grid(row=3, column=1, sticky="ew", pady=4, padx=(8, 0))

        # Marks Section
        ttk.Separator(self.left_frame, orient="horizontal").grid(
            row=4, column=0, columnspan=2, sticky="ew", pady=10
        )

        tk.Label(
            self.left_frame,
            text="Subject Marks (Out of 100)",
            font=("Segoe UI", 10, "bold"),
            bg="#FFFFFF",
            fg="#0F172A"
        ).grid(row=5, column=0, columnspan=2, sticky="w", pady=(0, 6))

        tk.Label(self.left_frame, text="Adv. Python:", bg="#FFFFFF").grid(row=6, column=0, sticky="w", pady=3)
        self.entry_python = ttk.Entry(self.left_frame, textvariable=self.var_mark_python, width=24, font=("Segoe UI", 9))
        self.entry_python.grid(row=6, column=1, sticky="ew", pady=3, padx=(8, 0))

        tk.Label(self.left_frame, text="DBMS:", bg="#FFFFFF").grid(row=7, column=0, sticky="w", pady=3)
        self.entry_dbms = ttk.Entry(self.left_frame, textvariable=self.var_mark_dbms, width=24, font=("Segoe UI", 9))
        self.entry_dbms.grid(row=7, column=1, sticky="ew", pady=3, padx=(8, 0))

        tk.Label(self.left_frame, text="Comp. Networks:", bg="#FFFFFF").grid(row=8, column=0, sticky="w", pady=3)
        self.entry_cn = ttk.Entry(self.left_frame, textvariable=self.var_mark_cn, width=24, font=("Segoe UI", 9))
        self.entry_cn.grid(row=8, column=1, sticky="ew", pady=3, padx=(8, 0))

        # Result Preview Card
        result_box = tk.Frame(self.left_frame, bg="#EFF6FF", bd=1, relief="groove", padx=8, pady=8)
        result_box.grid(row=9, column=0, columnspan=2, sticky="ew", pady=(10, 8))

        tk.Label(result_box, text="Percentage:", bg="#EFF6FF", font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky="w")
        self.lbl_pct_val = tk.Label(result_box, textvariable=self.var_percentage, bg="#EFF6FF", font=("Segoe UI", 10, "bold"), fg="#1E40AF")
        self.lbl_pct_val.grid(row=0, column=1, sticky="w", padx=6)

        tk.Label(result_box, text="Grade:", bg="#EFF6FF", font=("Segoe UI", 9, "bold")).grid(row=0, column=2, sticky="w", padx=(12, 0))
        self.lbl_grade_val = tk.Label(result_box, textvariable=self.var_grade, bg="#EFF6FF", font=("Segoe UI", 10, "bold"), fg="#059669")
        self.lbl_grade_val.grid(row=0, column=3, sticky="w", padx=6)

        btn_calc = tk.Button(
            self.left_frame,
            text="🧮 Preview % & Grade",
            command=self.handle_preview_calc,
            bg="#EEF2F6",
            fg="#1E293B",
            font=("Segoe UI", 8, "bold"),
            relief="groove",
            cursor="hand2"
        )
        btn_calc.grid(row=10, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        # Action Buttons
        btn_frame = tk.Frame(self.left_frame, bg="#FFFFFF")
        btn_frame.grid(row=11, column=0, columnspan=2, sticky="ew", pady=(5, 0))
        btn_frame.columnconfigure((0, 1), weight=1)

        self.btn_add = tk.Button(
            btn_frame,
            text="➕ Add Student",
            command=self.handle_add_student,
            bg="#2563EB",
            fg="#FFFFFF",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=6
        )
        self.btn_add.grid(row=0, column=0, padx=2, pady=3, sticky="ew")

        self.btn_update = tk.Button(
            btn_frame,
            text="✏️ Update",
            command=self.handle_update_student,
            bg="#0D9488",
            fg="#FFFFFF",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=6
        )
        self.btn_update.grid(row=0, column=1, padx=2, pady=3, sticky="ew")

        self.btn_delete = tk.Button(
            btn_frame,
            text="🗑️ Delete",
            command=self.handle_delete_student,
            bg="#DC2626",
            fg="#FFFFFF",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=6
        )
        self.btn_delete.grid(row=1, column=0, padx=2, pady=3, sticky="ew")

        self.btn_clear = tk.Button(
            btn_frame,
            text="🔄 Clear Form",
            command=self.clear_form,
            bg="#64748B",
            fg="#FFFFFF",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=6
        )
        self.btn_clear.grid(row=1, column=1, padx=2, pady=3, sticky="ew")

    def _build_search_and_table(self) -> None:
        """Build search controls and Treeview table."""
        search_card = tk.Frame(self.right_frame, bg="#FFFFFF", padx=12, pady=10, relief="solid", bd=1)
        search_card.pack(fill="x", pady=(0, 10))

        tk.Label(
            search_card,
            text="🔍 Search (ID / Name):",
            bg="#FFFFFF",
            font=("Segoe UI", 9, "bold"),
            fg="#334155"
        ).pack(side="left", padx=(0, 8))

        self.var_search = tk.StringVar()
        self.entry_search = ttk.Entry(search_card, textvariable=self.var_search, width=22, font=("Segoe UI", 9))
        self.entry_search.pack(side="left", padx=4)
        self.entry_search.bind("<Return>", lambda event: self.handle_search())

        tk.Button(
            search_card,
            text="Search",
            command=self.handle_search,
            bg="#3B82F6",
            fg="#FFFFFF",
            font=("Segoe UI", 8, "bold"),
            relief="flat",
            padx=10,
            pady=2,
            cursor="hand2"
        ).pack(side="left", padx=4)

        tk.Button(
            search_card,
            text="Show All",
            command=self.handle_reset_search,
            bg="#E2E8F0",
            fg="#1E293B",
            font=("Segoe UI", 8, "bold"),
            relief="flat",
            padx=10,
            pady=2,
            cursor="hand2"
        ).pack(side="left", padx=4)

        tk.Button(
            search_card,
            text="Top Performers (Sort %)",
            command=self.handle_sort_percentage,
            bg="#F3E8FF",
            fg="#6B21A8",
            font=("Segoe UI", 8, "bold"),
            relief="flat",
            padx=10,
            pady=2,
            cursor="hand2"
        ).pack(side="right", padx=4)

        table_card = tk.Frame(self.right_frame, bg="#FFFFFF", relief="solid", bd=1)
        table_card.pack(fill="both", expand=True)

        self.columns = (
            "id", "name", "class", "python", "dbms", "cn", "total", "percentage", "grade"
        )

        self.tree = ttk.Treeview(
            table_card,
            columns=self.columns,
            show="headings",
            selectmode="browse"
        )

        headings_map = {
            "id": ("Student ID", 80),
            "name": ("Name", 150),
            "class": ("Class / Div", 95),
            "python": ("Python", 65),
            "dbms": ("DBMS", 65),
            "cn": ("CN", 65),
            "total": ("Total / 300", 85),
            "percentage": ("Percentage", 85),
            "grade": ("Grade", 60),
        }

        for col, (heading_text, col_width) in headings_map.items():
            self.tree.heading(col, text=heading_text, anchor="center")
            self.tree.column(col, width=col_width, anchor="center")

        self.tree.column("name", anchor="w")

        y_scroll = ttk.Scrollbar(table_card, orient="vertical", command=self.tree.yview)
        x_scroll = ttk.Scrollbar(table_card, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")

        table_card.rowconfigure(0, weight=1)
        table_card.columnconfigure(0, weight=1)

        self.tree.bind("<ButtonRelease-1>", self.handle_row_selection)

    def _create_status_bar(self) -> None:
        """Create bottom status bar."""
        self.status_frame = tk.Frame(self.root, bg="#CBD5E1", height=24)
        self.status_frame.pack(fill="x", side="bottom")

        self.lbl_status_text = tk.Label(
            self.status_frame,
            text="Ready | Records loaded from storage",
            bg="#CBD5E1",
            font=("Segoe UI", 9),
            fg="#1E293B"
        )
        self.lbl_status_text.pack(side="left", padx=12)

        self.lbl_record_count = tk.Label(
            self.status_frame,
            text=f"Total Students: {self.storage.get_total_count()}",
            bg="#CBD5E1",
            font=("Segoe UI", 9, "bold"),
            fg="#1E293B"
        )
        self.lbl_record_count.pack(side="right", padx=15)

    def _extract_and_validate_inputs(self) -> tuple:
        """Extract and validate form inputs."""
        student_id = validate_student_id(self.var_id.get())
        name = validate_name(self.var_name.get())
        class_div = validate_class_div(self.var_class.get())

        marks_dict: Dict[str, float] = {
            "Advanced Python": validate_mark("Advanced Python", self.var_mark_python.get()),
            "DBMS": validate_mark("DBMS", self.var_mark_dbms.get()),
            "Computer Networks": validate_mark("Computer Networks", self.var_mark_cn.get()),
        }
        return student_id, name, class_div, marks_dict

    def handle_preview_calc(self) -> None:
        """Calculate and display percentage and grade preview."""
        try:
            p_val = validate_mark("Advanced Python", self.var_mark_python.get())
            d_val = validate_mark("DBMS", self.var_mark_dbms.get())
            c_val = validate_mark("Computer Networks", self.var_mark_cn.get())
            
            temp_marks = {"Advanced Python": p_val, "DBMS": d_val, "Computer Networks": c_val}
            temp_student = Student(student_id="TEMP", name="Temp", class_div="TEMP", marks=temp_marks)
            
            self.var_percentage.set(f"{temp_student.percentage}%")
            self.var_grade.set(temp_student.grade)
            self.set_status(f"Calculated: {temp_student.percentage}% | Grade: {temp_student.grade}")
        except ValidationError as ve:
            messagebox.showwarning("Validation Warning", str(ve))

    def handle_add_student(self) -> None:
        """Add new student record."""
        try:
            student_id, name, class_div, marks = self._extract_and_validate_inputs()
            new_student = Student(student_id=student_id, name=name, class_div=class_div, marks=marks)
            self.storage.add_student(new_student)

            self.refresh_table()
            self.clear_form()
            self.set_status(f"Student '{name}' (ID: {student_id}) added successfully!")
            messagebox.showinfo("Success", f"Student '{name}' added successfully!")
        except (ValidationError, DuplicateIDError) as err:
            messagebox.showerror("Error", str(err))
        except Exception as err:
            messagebox.showerror("Unexpected Error", f"An error occurred: {err}")

    def handle_update_student(self) -> None:
        """Update selected student record."""
        if not self.selected_student_id:
            messagebox.showwarning("Selection Required", "Please select a student from the table first.")
            return

        try:
            student_id, name, class_div, marks = self._extract_and_validate_inputs()

            if student_id != self.selected_student_id:
                confirm = messagebox.askyesno(
                    "ID Change Confirmation",
                    f"Change ID from '{self.selected_student_id}' to '{student_id}'?"
                )
                if not confirm:
                    return
                self.storage.delete_student(self.selected_student_id)

            updated_student = Student(student_id=student_id, name=name, class_div=class_div, marks=marks)

            if student_id == self.selected_student_id:
                self.storage.update_student(updated_student)
            else:
                self.storage.add_student(updated_student)

            self.refresh_table()
            self.clear_form()
            self.set_status(f"Student ID '{student_id}' updated successfully!")
            messagebox.showinfo("Success", f"Record for '{name}' updated successfully!")
        except (ValidationError, StudentNotFoundError, DuplicateIDError) as err:
            messagebox.showerror("Error", str(err))
        except Exception as err:
            messagebox.showerror("Error", f"Failed to update record: {err}")

    def handle_delete_student(self) -> None:
        """Delete selected student record after confirmation."""
        target_id = self.var_id.get().strip().upper() or self.selected_student_id
        if not target_id:
            messagebox.showwarning("Selection Required", "Please select a student record to delete.")
            return

        student = self.storage.get_student(target_id)
        if not student:
            messagebox.showerror("Not Found", f"No student found with ID '{target_id}'.")
            return

        if messagebox.askyesno("Confirm Delete", f"Delete student '{student.name}' (ID: {student.student_id})?"):
            try:
                self.storage.delete_student(student.student_id)
                self.refresh_table()
                self.clear_form()
                self.set_status(f"Student '{student.name}' deleted.")
                messagebox.showinfo("Deleted", "Student record successfully deleted.")
            except Exception as err:
                messagebox.showerror("Error", f"Failed to delete student: {err}")

    def handle_row_selection(self, event=None) -> None:
        """Populate form with selected row data."""
        selected_items = self.tree.selection()
        if not selected_items:
            return

        values = self.tree.item(selected_items[0], "values")
        if not values:
            return

        student = self.storage.get_student(str(values[0]))
        if not student:
            return

        self.selected_student_id = student.student_id
        self.var_id.set(student.student_id)
        self.var_name.set(student.name)
        self.var_class.set(student.class_div)

        marks = student.marks
        self.var_mark_python.set(str(marks.get("Advanced Python", "")))
        self.var_mark_dbms.set(str(marks.get("DBMS", "")))
        self.var_mark_cn.set(str(marks.get("Computer Networks", marks.get("CN", ""))))

        self.var_percentage.set(f"{student.percentage}%")
        self.var_grade.set(student.grade)
        self.set_status(f"Selected: {student.name} (ID: {student.student_id})")

    def handle_search(self) -> None:
        """Search students by ID or name."""
        query = self.var_search.get().strip()
        matched = self.storage.search_students(query)
        self.populate_treeview(matched)
        self.set_status(f"Search for '{query}' found {len(matched)} record(s).")

    def handle_reset_search(self) -> None:
        """Reset search and show all students."""
        self.var_search.set("")
        self.refresh_table()
        self.set_status("Displaying all student records.")

    def handle_sort_percentage(self) -> None:
        """Sort students by percentage (descending)."""
        sorted_students = self.storage.sort_students(by="percentage", reverse=True)
        self.populate_treeview(sorted_students)
        self.set_status("Sorted students by Percentage.")

    def refresh_table(self) -> None:
        """Reload and display all records."""
        self.populate_treeview(self.storage.get_all_students())

    def populate_treeview(self, students_list) -> None:
        """Populate Treeview rows."""
        for row in self.tree.get_children():
            self.tree.delete(row)

        for s in students_list:
            m = s.marks
            p_mark = m.get("Advanced Python", "-")
            d_mark = m.get("DBMS", "-")
            c_mark = m.get("Computer Networks", m.get("CN", "-"))
            total_mark = s.calculate_total_marks()

            self.tree.insert(
                "",
                "end",
                values=(
                    s.student_id,
                    s.name,
                    s.class_div,
                    p_mark,
                    d_mark,
                    c_mark,
                    f"{total_mark} / 300",
                    f"{s.percentage}%",
                    s.grade
                )
            )
        self.lbl_record_count.config(text=f"Total Students: {self.storage.get_total_count()}")

    def clear_form(self) -> None:
        """Reset form fields and selection."""
        self.selected_student_id = None
        self.var_id.set("")
        self.var_name.set("")
        self.var_class.set("")
        self.var_mark_python.set("")
        self.var_mark_dbms.set("")
        self.var_mark_cn.set("")
        self.var_percentage.set("-- %")
        self.var_grade.set("--")
        self.entry_id.focus_set()
        self.set_status("Form cleared. Ready for new input.")

    def set_status(self, message: str) -> None:
        """Update status bar text."""
        self.lbl_status_text.config(text=message)
