import Ecommerce.Product;
import Ecommerce.Customer;
import Ecommerce.Order;

public class TestEcommerce {
    public static void main(String[] args) {
        Product p = new Product("Laptop", 50000);
        Customer c = new Customer("Aashay");
        Order o = new Order(p, 2);

        c.displayCustomer();
        o.displayOrder();
    }
}