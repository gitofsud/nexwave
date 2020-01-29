import java.util.Scanner;

class Book {
	String title;
	String author;
	double cost;
	int no_of_books;

	public Book(String title, String author, double cost, int no_of_books) {
		this.title = title;
		this.author = author;
		this.cost = cost;
		this.no_of_books = no_of_books;
	}

	void display() {
		System.out.println("Title: " + title + ", Author: " + author);
		System.out.println("Cost: " + cost);
	}
}

public class Q4 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter data for books.");
		Book x[] = new Book[3];
		
		for (int i = 0; i < 3; i++) {
			System.out.print("Enter title: ");
			String title = sc.next();
			System.out.print("Enter author: ");
			String author = sc.next();
			System.out.print("Enter cost: ");
			double cost = sc.nextDouble();
			System.out.print("Enter no of books: ");
			int no_of_books = sc.nextInt();
			x[i] = new Book(title, author, cost, no_of_books);
		}

		System.out.print("\nEnter title to search: ");
		String title = sc.next();
		System.out.print("Enter no of books required: ");
		int no_of_books = sc.nextInt();

		boolean found = false;
		for (int i = 0; i < 3; i++) {
			if (title.equals(x[i].title) && (no_of_books <= x[i].no_of_books)) {
				found = true;
				x[i].display();
				System.out.println("Books are sufficient.");
				System.out.println("Total cost of books: " + (x[i].cost * no_of_books));
			}
		}

		if (found == false) {
			System.out.println("No books found.");
		}
	}
}
