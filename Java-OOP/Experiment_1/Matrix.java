public class Matrix {
    public static void main(String[] args) {

        int a[][] = { {1, 2}, {3, 4} };
        int b[][] = { {5, 6}, {7, 8} };
        int c[][] = new int[2][2];

        int choice = 3;

        switch (choice) {

            case 1:
                for (int i = 0; i < 2; i++) {
                    for (int j = 0; j < 2; j++) {
                        c[i][j] = a[i][j] + b[i][j];
                    }
                }
                System.out.println("Addition:");
                break;

            case 2:
                for (int i = 0; i < 2; i++) {
                    for (int j = 0; j < 2; j++) {
                        c[i][j] = a[i][j] - b[i][j];
                    }
                }
                System.out.println("Subtraction:");
                break;

            case 3:
                for (int i = 0; i < 2; i++) {
                    for (int j = 0; j < 2; j++) {
                        c[i][j] = 0;
                        for (int k = 0; k < 2; k++) {
                            c[i][j] += a[i][k] * b[k][j];
                        }
                    }
                }
                System.out.println("Multiplication:");
                break;

            case 4:
                System.out.println("Transpose:");
                for (int i = 0; i < 2; i++) {
                    for (int j = 0; j < 2; j++) {
                        System.out.print(a[j][i] + " ");
                    }
                    System.out.println();
                }
                return;

            default:
                System.out.println("Invalid choice");
                return;
        }

        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                System.out.print(c[i][j] + " ");
            }
            System.out.println();
        }
    }
}
