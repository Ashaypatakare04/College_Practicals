import java.io.*;
import java.util.Scanner;

public class StudentFile {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.print("Name: ");
            String name = sc.nextLine();

            System.out.print("Age: ");
            int age = sc.nextInt();

            System.out.print("Weight: ");
            double weight = sc.nextDouble();

            System.out.print("Height: ");
            double height = sc.nextDouble();
            sc.nextLine();

            System.out.print("City: ");
            String city = sc.nextLine();

            System.out.print("Phone: ");
            String phone = sc.nextLine();

            BufferedWriter bw = new BufferedWriter(new FileWriter("sample.txt"));
            bw.write("Name: " + name);
            bw.newLine();
            bw.write("Age: " + age);
            bw.newLine();
            bw.write("Weight: " + weight);
            bw.newLine();
            bw.write("Height: " + height);
            bw.newLine();
            bw.write("City: " + city);
            bw.newLine();
            bw.write("Phone: " + phone);
            bw.close();

            BufferedReader br = new BufferedReader(new FileReader("sample.txt"));
            String line;
            System.out.println("\nStored Data:");
            while ((line = br.readLine()) != null)
                System.out.println(line);
            br.close();

        } catch (Exception e) {
            System.out.println(e);
        }
        sc.close();
    }
}
