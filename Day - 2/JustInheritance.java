class A {
	A() {
		System.out.println("A");
	}
}

class B extends A {
	B() {
		System.out.println("B");
	}
}

class C extends B {
	C() {
		super();
		System.out.println("C");
	}
}

public class JustInheritance {
	public static void main(String[] args) {
		C c = new C();
	}
}
