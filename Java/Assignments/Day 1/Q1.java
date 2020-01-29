
public class Q1 {
	public static void Part1() {
		for (int i = 0; i < 6; i++) {
			for (int j = 0; j <= i; j++) {
				if (i % 2 == 0)
					System.out.print("*");
				else
					System.out.print("+");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		Part1();
	}
}
