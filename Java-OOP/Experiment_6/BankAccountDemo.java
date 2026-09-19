class LowBalanceException extends Exception {
    LowBalanceException(String msg) {
        super(msg);
    }
}

class NegativeNumberException extends Exception {
    NegativeNumberException(String msg) {
        super(msg);
    }
}

class BankAccount {
    double balance = 5000;

    void balanceEnquiry() {
        System.out.println("Balance: " + balance);
    }

    void deposit(double amt) throws NegativeNumberException {
        if (amt < 0)
            throw new NegativeNumberException("Negative amount not allowed");
        balance += amt;
    }

    void withdraw(double amt)
            throws LowBalanceException, NegativeNumberException {

        if (amt < 0)
            throw new NegativeNumberException("Negative amount not allowed");

        if (amt > balance)
            throw new LowBalanceException("Insufficient balance");

        balance -= amt;
    }
}

public class BankAccountDemo {
    public static void main(String[] args) {
        BankAccount b = new BankAccount();

        try {
            b.balanceEnquiry();
            b.deposit(1000);
            b.withdraw(7000);   
        }
        catch (Exception e) {
            System.out.println("Exception: " + e.getMessage());
        }
    }
}