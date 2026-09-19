import java.util.Scanner;

public class Area{
int length;
int breadth;

void setDim(){
Scanner sc=new Scanner(System.in);
length=sc.nextInt();
breadth=sc.nextInt();
}

void getarea(){
System.out.println("Area of rectangle: "+(length*breadth));
}

public static void main(String[] args){
Area a=new Area();
a.setDim();
a.getarea();
}
}
