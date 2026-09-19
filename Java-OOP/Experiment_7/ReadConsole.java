import java.io.*;
import java.util.Scanner;
public class ReadConsole{
 public static void main(String args[]) {
 try{
 
File file = new File("sample.txt");
Scanner dataReader = new Scanner(file);
while(dataReader.hasNextLine()){
String filedata= dataReader.nextLine();
 System.out.println(filedata);
 }
 dataReader.close();
 }
 catch(FileNotFoundException exception){
 System.out.println("Unexpected error occured!");
 exception.printStackTrace();
 }
 }
 }
