def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")

    file = open("books.txt", "a")
    file.write(book_id + "," + title + "," + author + ",Available\n")
    file.close()

    print("Book added successfully.")


def search_book():
    book_id = input("Enter Book ID to search: ")

    file = open("books.txt", "r")

    found = False

    for line in file:
        book = line.strip().split(",")

        if book[0] == book_id:
            print("Book ID:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            print("Status:", book[3])
            found = True
            break

    file.close()

    if not found:
        print("Book not found.")


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()

    found = False

    for i in range(len(lines)):
        book = lines[i].strip().split(",")

        if book[0] == book_id:
            found = True

            if book[3] == "Available":
                book[3] = "Issued"
                lines[i] = ",".join(book) + "\n"
                print("Book issued successfully.")
            else:
                print("Book is already issued.")

    file = open("books.txt", "w")
    file.writelines(lines)
    file.close()

    if not found:
        print("Book not found.")


def return_book():
    book_id = input("Enter Book ID to return: ")

    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()

    found = False

    for i in range(len(lines)):
        book = lines[i].strip().split(",")

        if book[0] == book_id:
            found = True

            if book[3] == "Issued":
                book[3] = "Available"
                lines[i] = ",".join(book) + "\n"
                print("Book returned successfully.")
            else:
                print("Book is already available.")

    file = open("books.txt", "w")
    file.writelines(lines)
    file.close()

    if not found:
        print("Book not found.")


def display_available_books():
    file = open("books.txt", "r")

    print("\nAvailable Books:")

    for line in file:
        book = line.strip().split(",")

        if book[3] == "Available":
            print(book[0], book[1], book[2])

    file.close()


# Menu
while True:
    print("\n--- BOOK MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        display_available_books()
    elif choice == "6":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")