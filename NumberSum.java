public class NumberSum {

    public static void main(String...args){

        int totalSum = 0; 

        int evenSum = 0;

        int oddSum = 0;

        
        for (int index = 1; index <= 20; index+=2) {
            totalSum += index;

            
            if (index % 2 == 0) {
                evenSum += index;  
            } else {
                oddSum += index; 
           }
         }
        
        System.out.println("Total Sum of numbers: " + totalSum);

        System.out.println("Sum of Even numbers: " + evenSum);

        System.out.println("Sum of Odd numbers: " + oddSum);
  
      }

   }
