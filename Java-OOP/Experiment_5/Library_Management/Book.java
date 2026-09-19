package LibraryManagement;

public class Book {
    String title, author, isbn;

    public Book(String t, String a, String i) {
        title = t;
        author = a;
        isbn = i;
    }

    public void displayBook() {
        System.out.println(title + " " + author + " " + isbn);
    }
}
