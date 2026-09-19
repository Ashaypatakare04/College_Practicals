abstract class Shape {
    double dim1, dim2;

    Shape(double dim1, double dim2) {
        this.dim1 = dim1;
        this.dim2 = dim2;
    }

    abstract double area();
}

class Rectangle extends Shape {
    Rectangle(double l, double b) {
        super(l, b);
    }

    double area() {
        return dim1 * dim2;
    }
}

class Triangle extends Shape {
    Triangle(double b, double h) {
        super(b, h);
    }

    double area() {
        return 0.5 * dim1 * dim2;
    }
}

class TestShape {
    public static void main(String[] args) {
        Rectangle r = new Rectangle(10, 5);
        Triangle t = new Triangle(10, 5);

        System.out.println("Rectangle Area: " + r.area());
        System.out.println("Triangle Area: " + t.area());
    }
}