package StudentPackage;

public class RegisterStudent {

	void total(int cd) {
		int TotalCredits = cd;
		try {
			if (TotalCredits > 30) {
				throw new CreditLimit(TotalCredits);
			} else {
				System.out.println("The Total credit is:" + TotalCredits);
			}
		} catch (Exception e) {
			System.out.println("Total Credits is more than 30");
		}
	}
}