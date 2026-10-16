//import java.util.Scanner;
//import java.util.Arrays;
//public class Array{
//
//public static void main(String...args){
//
//Scanner input = new Scanner (System.in);
//
//int [] numbers = new int [5];
//
//int [] scores = {3, 5, 7, 8, 9};
//
//for (int index = 0; index < numbers.length; index++){
//
//    System.out.println("Enter a number: ");
//    int number = input.nextInt();
//    numbers[index] = number;
//}
//
//System.out.println(Arrays.toString(numbers));
//
//   }
//
//
// } 
import java.util.Scanner;
import java.util.Arrays;

public class Array{

public static void main(String...args){

Scanner input = new Scanner(System.in);

String [] names = new String [7];


for(int index = 0; index < names.length; index++) {

   System.out.println("Enter  names: ");

   String name  = input.nextLine();

    names[index] = name;
     
     }

System.out.println(Arrays.toString(names));



   

   }

  }
