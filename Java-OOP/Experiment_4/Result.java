class Student {
    int rollNo;

    void setRollNo(int r) {
        rollNo = r;
    }

    int getRollNo() {
        return rollNo;
    }
}

class Test extends Student {
    int sub1, sub2;

    void setMarks(int m1, int m2) {
        sub1 = m1;
        sub2 = m2;
    }

    void getMarks() {
        System.out.println("Marks: " + sub1 + " " + sub2);
    }
}

interface Sports {
    int sMarks = 10;
    void set();
}

class Result extends Test implements Sports {
    int total;

    public void set() {
        total = sub1 + sub2 + sMarks;
    }

    void display() {
        System.out.println("Roll No: " + rollNo);
        System.out.println("Total: " + total);
    }

    public static void main(String[] args) {
        Result r = new Result();
        r.setRollNo(1);
        r.setMarks(80, 85);
        r.getMarks();
        r.set();
        r.display();
    }
}