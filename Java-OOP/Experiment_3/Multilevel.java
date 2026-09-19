public class Multilevel {
    
}
class Student {
    int roll_no;
    
    Student(int roll_no) {
        this.roll_no = roll_no;
    }
}

class Test extends Student {
    double sub1, sub2;
    
    Test(int roll_no, double sub1, double sub2) {
        super(roll_no);
        this.sub1 = sub1;
        this.sub2 = sub2;
    }
}

class Result extends Test {
    Result(int roll_no, double sub1, double sub2) {
        super(roll_no, sub1, sub2);
    }
    void displayResult() {
        double average = (sub1 + sub2) / 2;
        System.out.println("Roll No: " + roll_no);
        System.out.println("Subject 1: " + sub1);
        System.out.println("Subject 2: " + sub2);
        System.out.println("Average: " + average);
    }
    
    public static void main(String[] args) {
        Result r = new Result(101, 85.5, 92.0);
        r.displayResult();
    }
}

