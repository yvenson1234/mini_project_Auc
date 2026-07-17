class LibraryPresenter:
    
    def present_success(self, message: str) -> str:
        return f"[SUCCESS] {message}"

    def present_error(self, error_message: str) -> str:
        return f"[ERROR] {error_message}"

    def present_info(self, info_message: str) -> str:
        return f"[INFO] {info_message}"

    def present_book_list(self, books) -> str:
        if not books:
            return "No books registered in the cafeteria library yet."
        
        output = []
        output.append("\n")
        output.append("    ")
        output.append("")
        for book in books:
            output.append(
                f" ID: {book.id:<3} | Title: {book.title:<28} | "
                f"Author: {book.author:<18} | Status: {book.status}"
            )
        output.append("\n")
        return "\n".join(output)

    def present_search_results(self, title: str, books) -> str:
        if not books:
            return self.present_info(f"No books found matching '{title}'.")
        
        output = []
        output.append(f"\n--- SEARCH RESULTS FOR '{title}'")
        for book in books:
            output.append(f" ID: {book.id} | '{book.title}' by {book.author} ({book.status})")
        output.append("\n")
        return "\n".join(output)