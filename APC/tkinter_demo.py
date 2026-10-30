from tkinter import *

root = Tk()
root.title("Addition")

Label(root, text="Enter First Number").pack()
e1 = Entry(root)
e1.pack()

Label(root, text="Enter Second Number").pack()
e2 = Entry(root)
e2.pack()

def add():
    result = int(e1.get()) + int(e2.get())
    Label(root, text="Result: " + str(result)).pack()

Button(root, text="Add", command=add).pack()

root.mainloop()
