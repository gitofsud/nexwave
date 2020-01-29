import java.util.Scanner;

class Book {
	String title;
	String author;
	double cost;
	int no_of_books;

	void display() {
		System.out.println("Title: " + title + ", Author: " + author);
		System.out.println("Cost: " + cost + ", No of Books: " + no_of_books);
	}
}

public class Q4 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		Book a = new Book();
		Book b = new Book();
		Book c = new Book();

		System.out.print("Enter title: ");
		a.title = sc.nextLine();
		System.out.print("Enter author: ");
		a.author = sc.nextLine();
		System.out.print("Enter cost: ");
		a.cost = sc.nextDouble();
		System.out.print("Enter no of books: ");
		a.no_of_books = sc.nextInt();
	}
}
