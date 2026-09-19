package ExceptionHandlingDemo;

class DivisionException extends Exception {
    DivisionException(String msg) {
        super(msg);
    }
}

class Calculator {
    int divide(int a, int b) throws DivisionException {
        if (b == 0)
            throw new DivisionException("Cannot divide by zero");
        return a / b;
    }
}

public class DivisionDemo {
    public static void main(String[] args) {
        Calculator c = new Calculator();

        try {
            System.out.println("Result: " + c.divide(10, 0));
        }
        catch (DivisionException e) {
            System.out.println("Exception: " + e.getMessage());
        }
    }

}
