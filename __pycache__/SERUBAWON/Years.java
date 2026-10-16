import java.util.Scanner;
public class Years{
public static void main(String[] args){
Scanner input = new Scanner(System.in);
System.out.print("Enter the first name: ");
String firstname = input.nextLine();
System.out.print("Enter the last name: ");
String lastname = input.nextLine();
System.out.print("year of birth: ");
int birthyear = input.nextInt();
int currentyear = 2025;
int age = currentyear-birthyear;
System.out.println("Hello " + firstname + " " + lastname +",");
System.out.println("You are" + age + "Years old.");
}
} 
