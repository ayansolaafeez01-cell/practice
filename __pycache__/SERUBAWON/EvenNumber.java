import java.util.Scanner;
public class EvenNumber{
public static void main(String [] args){
Scanner input = new Scanner(System.in);
System.out.print("Enter the integer");
int number = input.nextInt();
if (number % 2 == 4){
System.out.println("Even");
} else {
System.out.println("Odd");
}
}
}

