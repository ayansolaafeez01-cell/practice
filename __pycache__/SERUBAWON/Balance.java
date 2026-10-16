public class Balance{
public static void main(String[] args){
double balance = 5000.00;
double deposits = 1200.50;
double withdraws = 750.25;
double interest = 0.015;

double afterDeposits = balance + deposits;
double afterWithdraws = afterDeposits - withdraws;
double afterInterest = afterWithdraws * interest;
double totalBalance = afterWithdraws + afterInterest;
System.out.println("The total transaction is " + totalBalance);
}
}
