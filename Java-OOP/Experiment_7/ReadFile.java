import java.io.*;
import java.util.Scanner;

public class ReadFile{
 public static void main(String args[]) {
 int vowels=0,words=0,countA=0;
 try{
 
BufferedReader file = new BufferedReader(
new FileReader("sample.txt"));

String line;

while((line=file.readLine())!=null){

String[] filedata= line.split("\\s+");
words +=filedata.length;

for(int i=0;i<line.length();i++){
char ch =Character.toLowerCase(line.charAt(i));

if("aeiou".indexOf(ch)!=-1){
vowels++;
}
if(ch=='a'){
countA++;}
}
}
file.close();

 System.out.println("Total Vowels: "+vowels);
  System.out.println("Total Words: "+words);
   System.out.println("Total A: "+countA);
 }
 
 catch(Exception e){
 System.out.println("Unexpected error occured!" + e);
 }
 }
 }
