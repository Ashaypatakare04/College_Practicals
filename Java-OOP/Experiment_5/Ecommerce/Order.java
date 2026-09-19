package Ecommerce;

public class Order {
    Product product;
    int quantity;

    public Order(Product p, int q) {
        product = p;
        quantity = q;
    }

    public double calculateTotal() {
        return product.price * quantity;
    }

    public void displayOrder() {
        product.displayProduct();
        System.out.println("Quantity: " + quantity);
        System.out.println("Total: " + calculateTotal());
    }
}