package Ecommerce;

public class Customer {
    String name;

    public Customer(String n) {
        name = n;
    }

    public void displayCustomer() {
        System.out.println(name);
    }
}