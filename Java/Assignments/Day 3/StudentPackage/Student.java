package StudentPackage;

import java.util.Scanner;

public class Student {
	static Scanner s;

	public static void main(String[] args) {
		s = new Scanner(System.in);
		System.out.println("Enter the total credit:");
		int c = Integer.parseInt(s.next());
		RegisterStudent r = new RegisterStudent();
		r.total(c);
	}
}
