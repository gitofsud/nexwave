import java.util.Scanner;

public class Q5 {
	public static int getMin(int a, int b, int c) {
		return Math.min(a, Math.min(b, c));
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter three numbers: ");
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		System.out.println(getMin(a, b, c));
	}
}
