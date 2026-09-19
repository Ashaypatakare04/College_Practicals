import LibraryManagement.Book;
import LibraryManagement.Member;

public class TestLibrary {
    public static void main(String[] args) {
        Book b = new Book("Java", "James", "12345");
        Member m = new Member("Aashay", 1);

        b.displayBook();
        m.displayMember();
    }
}
