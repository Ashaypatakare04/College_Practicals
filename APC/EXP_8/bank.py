class BankAccount:
    account_counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} deposited successfully.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully.")
        else:
            print("Error: Insufficient balance.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")

    def transfer(self, amount, other_account):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print(f"Amount {amount} transferred successfully.")
        else:
            print("Error: Insufficient balance for transfer.")


account1 = BankAccount("Customer 1")
account2 = BankAccount("Customer 2")

account1.deposit(5000)
account1.withdraw(1000)
account1.display_balance()

print("/n")

account2.deposit(10000)
account2.withdraw(2000)
account2.display_balance()

print()

account1.transfer(2000, account2)

print("\nAfter Transfer:")
account1.display_balance()
print()
account2.display_balance()
