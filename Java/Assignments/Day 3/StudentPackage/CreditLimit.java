package StudentPackage;

public class CreditLimit extends Exception {
	CreditLimit(int i) {
		System.out.println("The Total credit is:" + i);
	}
}