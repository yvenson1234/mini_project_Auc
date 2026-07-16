from src.use_cases.add_book import AddBookOutput
from src.use_cases.list_books import ListBooksOutput

class BookPresenter:
    def format_add_book(self, output: AddBookOutput) -> str:
        if not output.success:
            return f" error: {output.message}"
        book = output.book
        return f"book add with success\n   Tit: {book.title}\n   Otè: {book.author}\n   ID: {book.id}"

    def format_list_books(self, output: ListBooksOutput) -> str:
        if not output.success:
            return f"error: {output.message}"
        if not output.books:
            return " Pa gen okenn liv nan bibliyotèk la kounye a."
        
        result = "list book:\n"
        for book in output.books:
            result += f"  - [{book.status.value}] {book.title} (pa {book.author}) | ID: {book.id}\n"
        return result