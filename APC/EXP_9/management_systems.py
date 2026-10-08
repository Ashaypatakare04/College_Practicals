balance = 0
transactions = []
books = {}

def deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposited " + str(amount))

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn " + str(amount))
        return True
    return False

def balance_enquiry():
    return balance

def transaction_history():
    return transactions

def add_book(book):
    books[book] = True

def issue_book(book):
    if book in books and books[book]:
        books[book] = False
        return True
    return False

def return_book(book):
    if book in books:
        books[book] = True
        return True
    return False

def search_book(book):
    return book in books

def available_books():
    return [book for book in books if books[book]]

print("Banking System")
deposit(5000)
print("Withdrawal Successful:", withdraw(1000))
print("Current Balance:", balance_enquiry())
print("Transaction History:", transaction_history())

print()
print("Library System")
add_book("Python")
add_book("AI")
print("Book Issued:", issue_book("Python"))
print("Available Books:", available_books())
return_book("Python")
print("Available Books After Return:", available_books())
