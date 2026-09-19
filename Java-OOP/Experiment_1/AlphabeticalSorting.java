import java.util.Arrays;

public class AlphabeticalSorting{
public static void main(String[] args){
String[] names={"Ashay","Pratik","Pranav","Soham","Ganesh","Meenakshi","Ratnesh","Ritesh","Siddhesh","Sahil"};

Arrays.sort(names);
for(String name:names){
System.out.println(name);
}
}
}
