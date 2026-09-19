interface Shape {
    double area();
}

class Rectangle implements Shape {
    double length, breadth;

    Rectangle(double l, double b) {
        length = l;
        breadth = b;
    }

    public double area() {
        return length * breadth;
    }
}

class Triangle implements Shape {
    double base, height;

    Triangle(double b, double h) {
        base = b;
        height = h;
    }

    public double area() {
        return 0.5 * base * height;
    }
}

class TestShape2 {
    public static void main(String[] args) {
        Rectangle r = new Rectangle(10, 5);
        Triangle t = new Triangle(10, 5);

        System.out.println("Rectangle Area: " + r.area());
        System.out.println("Triangle Area: " + t.area());
    }
}