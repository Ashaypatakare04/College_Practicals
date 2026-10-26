"""
main.py
Main entry point for the Student Record Management System.
Subject: Advanced Programming Concepts (Python) [231CSEPCC304]
Semester: V | TY B.Tech CSE (NEP Curriculum)

To run the project:
    python main.py
"""

import sys
import tkinter as tk
from gui import StudentManagementApp


def setup_windows_dpi():
    """Enable crisp font rendering on high-DPI Windows screens if possible."""
    if sys.platform.startswith("win"):
        try:
            import ctypes
            # Shcore process DPI awareness: 1 = Process_System_DPI_Aware, 2 = Process_Per_Monitor_DPI_Aware
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            try:
                # Fallback for older Windows versions
                ctypes.windll.user32.SetProcessDPIAware()
            except Exception:
                pass


def main():
    """Main application launcher."""
    # Configure High DPI for Windows
    setup_windows_dpi()

    # Create root Tkinter window
    root = tk.Tk()

    # Instantiate Application
    app = StudentManagementApp(root)

    # Start Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
