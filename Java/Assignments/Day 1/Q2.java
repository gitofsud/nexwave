class Ob {
	static int count = 0;

	Ob() {
		count++;
	}
}

public class Q2 {
	public static void main(String[] args) {
		Ob a = new Ob();
		System.out.println("Count: " + Ob.count);
		Ob b = new Ob();
		System.out.println("Count: " + Ob.count);
	}
}
