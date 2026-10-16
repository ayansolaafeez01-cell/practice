import java.util.Scanner;

public class TaskOne{

    public static  void main(String...args){

        Scanner input = new Scanner(System.in);

        System.out.print("Enter your name: ");

        String name = input.nextLine();

        System.out.println("Enter your age: ");

        int age = input.nextInt();

       

        System.out.printf("your name is %s you are %d years old\n", name, age);
}

}
