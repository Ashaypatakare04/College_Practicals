class OddNumberException extends Exception {
    OddNumberException(String msg) {
        super(msg);
    }
}

public class OddNumberDemo {

    static void check(int num) throws OddNumberException {
        if (num % 2 != 0)
            throw new OddNumberException("Number is odd");
        System.out.println("Number is even");
    }

    public static void main(String[] args) {
        try {
            check(5);           }
        catch (OddNumberException e) {
            System.out.println("Exception: " + e.getMessage());
        }
    }
}