class Employee {
    String name, address, jobTitle;
    double salary;

    Employee(String name, String address, double salary, String jobTitle) {
        this.name = name;
        this.address = address;
        this.salary = salary;
        this.jobTitle = jobTitle;
    }

    double calculateBonus() {
        return salary * 0.10;
    }

    void performanceReport() {
        System.out.println(name + " Performance is good");
    }

    void manageProject() {
        System.out.println(name + " is managing project");
    }
}

class Manager extends Employee {
    Manager(String name, String address, double salary) {
        super(name, address, salary, "Manager");
    }

    double calculateBonus() {
        return salary * 0.20;
    }
}

class Developer extends Employee {
    Developer(String name, String address, double salary) {
        super(name, address, salary, "Developer");
    }

    double calculateBonus() {
        return salary * 0.15;
    }
}

class Programmer extends Employee {
    Programmer(String name, String address, double salary) {
        super(name, address, salary, "Programmer");
    }

    double calculateBonus() {
        return salary * 0.12;
    }
}

class TestEmployee {
    public static void main(String[] args) {
        Manager m = new Manager("A", "Kolhapur", 50000);
        Developer d = new Developer("B", "Pune", 40000);
        Programmer p = new Programmer("C", "Mumbai", 30000);

        System.out.println("Manager Bonus: " + m.calculateBonus());
        System.out.println("Developer Bonus: " + d.calculateBonus());
        System.out.println("Programmer Bonus: " + p.calculateBonus());
    }
}