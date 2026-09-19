class BankAccount {
    protected double balance;

    public BankAccount(double balance) {
        this.balance = balance;
    }

    public void deposit(double amount) {
        balance += amount;
        System.out.println("Balance: " + balance);
    }

    public void withdraw(double amount) {
        balance -= amount;
        System.out.println("Balance: " + balance);
    }
}

class SavingsAccount extends BankAccount {
    public SavingsAccount(double balance) {
        super(balance);
    }

    public void withdraw(double amount) {
        if (balance - amount < 100) {
            System.out.println("Minimum balance of 100 required");
        } else {
            balance -= amount;
            System.out.println("Balance: " + balance);
        }
    }

    public static void main(String[] args) {
        SavingsAccount obj = new SavingsAccount(500);
        obj.deposit(200);
        obj.withdraw(550);
        obj.withdraw(100);
    }
}