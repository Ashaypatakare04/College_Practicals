package Ecommerce;

public class Product {
    String name;
    double price;

    public Product(String n, double p) {
        name = n;
        price = p;
    }

    public void displayProduct() {
        System.out.println(name + " " + price);
    }
}
