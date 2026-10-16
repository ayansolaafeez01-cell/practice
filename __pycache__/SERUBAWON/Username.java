import java.util.Scanner;

public class Username{

public static void main (String [] args){

Scanner input = new Scanner (System.in)[

System.out.print("Enter usernsame: ");

String username = input.nextLine();

System.out.print("Enter password: ");

String password = input.nextLine();

if(username.equals("admin")){

if(password.equals("1234")){

System.out.println("Access granted");

} else {

System.out.println("Access denied");

} else {

System.out.println("Access denied");

}

}
}
}
