import MathOperations.Operations;

public class TestMath {
    public static void main(String[] args) {
        Operations op = new Operations();

        double num = 5.7;

        System.out.println("Floor: " + op.floorValue(num));
        System.out.println("Ceil: " + op.ceilValue(num));
        System.out.println("Round: " + op.roundValue(num));
    }
}
