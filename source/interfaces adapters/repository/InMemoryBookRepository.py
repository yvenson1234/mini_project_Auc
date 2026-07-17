from interfaces.book_repository import BookRepository

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books = {}

    def add(self, book):
        self.books[book.id] = book

    def update(self, book):
        if book.id in self.books:
            self.books[book.id] = book

    def get_by_id(self, book_id):
        return self.books.get(book_id)

    def list_all(self):
        return list(self.books.values())

    def search_by_title(self, title):
        results = []
        for book in self.books.values():
            if title.lower() in book.title.lower():
                results.append(book)
        return results