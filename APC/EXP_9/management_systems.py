balance = 0
transactions = []
books = {}

def q24_deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposited " + str(amount))

def q24_withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn " + str(amount))
        return True
    return False

def q24_balance_enquiry():
    return balance

def q24_transaction_history():
    return transactions

def q25_add_book(book):
    books[book] = True

def q25_issue_book(book):
    if book in books and books[book]:
        books[book] = False
        return True
    return False

def q25_return_book(book):
    if book in books:
        books[book] = True
        return True
    return False

def q25_search_book(book):
    return book in books

def q25_available_books():
    return [book for book in books if books[book]]

if __name__ == "__main__":
    q24_deposit(5000)
    print(q24_withdraw(1000))
    print(q24_balance_enquiry())
    print(q24_transaction_history())

    q25_add_book("Python")
    q25_add_book("AI")
    print(q25_issue_book("Python"))
    print(q25_available_books())
    q25_return_book("Python")
    print(q25_available_books())
