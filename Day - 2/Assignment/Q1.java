import java.util.Scanner;

class Account {
	int accno;
	String name;
	int phone_no;
	float balance_amt;

	void getInput() {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter account no: ");
		accno = sc.nextInt();
		System.out.print("Enter name: ");
		name = sc.next();
		System.out.print("Enter phone: ");
		phone_no = sc.nextInt();
		System.out.print("Enter balance amount: ");
		balance_amt = sc.nextFloat();
	}

	void deposit(float amt) {
		balance_amt += amt;
		System.out.println("Balance: " + balance_amt);
	}

	void withdraw(float amt) {
		balance_amt -= amt;
		System.out.println("Balance: " + balance_amt);
	}
}

public class Q1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Account x = new Account();
		x.getInput();
		System.out.println("Enter amount to deposit: ");
		float dep = sc.nextFloat();
		x.deposit(dep);
		System.out.println("Enter amount to withdraw: ");
		float wid = sc.nextFloat();
		x.withdraw(wid);
	}
}
