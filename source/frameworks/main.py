import sys
from adapters.in_memory_book_repository import InMemoryBookRepository
from adapters.in_memory_reservation_repository import InMemoryReservationRepository
from adapters.library_presenter import LibraryPresenter
from adapters.library_controller import LibraryController

def main():
    book_repository = InMemoryBookRepository()
    reservation_repository = InMemoryReservationRepository()
    presenter = LibraryPresenter()
    controller = LibraryController(book_repository, reservation_repository, presenter)

    while True:
        print("\n")
        print(" ")
        print("")
        print(" 1. Add a Book")
        print(" 2. List All Books")
        print(" 3. Search a Book by Title")
        print(" 4. Reserve a Book")
        print(" 5. Return a Book")
        print(" 6. Cancel a Reservation")
        print(" 7. Exit")
        print("")
        
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            print("\n--- Add a New Book ---")
            try:
                book_id = int(input("Enter Book ID: ").strip())
                title = input("Enter Book Title: ").strip()
                author = input("Enter Book Author: ").strip()
                print("Categories: EXACT_SCIENCE, LIFE_SCIENCES, HUMANITIES, SOCIAL_SCIENCES, COMPUTER_SCIENCE, MEDICINE_AND_HEALTH...")
                category = input("Enter Category: ").strip()
                print(controller.add_book(book_id, title, author, category))
            except ValueError:
                print("[ERROR] ID must be a valid number.")

        elif choice == "2":
            print(controller.list_all_books())

        elif choice == "3":
            print("\n--- Search Book ---")
            title = input("Enter search title: ").strip()
            print(controller.search_book(title))

        elif choice == "4":
            print("\n--- Reserve a Book ---")
            try:
                res_id = int(input("Enter Reservation ID: ").strip())
                book_title = input("Enter Book Title to Reserve: ").strip()
                user_id = int(input("Enter Your Student ID: ").strip())
                print(controller.reserve_book(res_id, book_title, user_id))
            except ValueError:
                print("[ERROR] IDs must be valid numbers.")

        elif choice == "5":
            print("\n--- Return a Book ---")
            try:
                book_id = int(input("Enter Book ID to Return: ").strip())
                print(controller.return_book(book_id))
            except ValueError:
                print("[ERROR] Book ID must be a valid number.")

        elif choice == "6":
            print("\n--- Cancel a Reservation ---")
            book_title = input("Enter Book Title: ").strip()
            print(controller.cancel_reservation(book_title))

        elif choice == "7":
            print("\nGoodbye! Thank you for using AUC Cafeteria Library System.")
            sys.exit()

        else:
            print("\n[ERROR] Invalid option. Please select between 1 and 7.")

if __name__ == "__main__":
    main()