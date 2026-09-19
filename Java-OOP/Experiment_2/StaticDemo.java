public class StaticDemo{
static int count;

static{
count=10;
System.out.println("Static block");
}

static void show(){
System.out.println("Static method");
System.out.println("Count: "+count);
}

public static void main(String[] args){
System.out.println("------");
StaticDemo.show();
}
}
