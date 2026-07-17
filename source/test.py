import sys
from src.adapters.in_memory_book_repository import InMemoryBookRepository
from src.adapters.in_memory_reservation_repository import InMemoryReservationRepository
from src.adapters.library_presenter import LibraryPresenter
from src.adapters.library_controller import LibraryController

def run_tests():
    book_repo = InMemoryBookRepository()
    reservation_repo = InMemoryReservationRepository()
    presenter = LibraryPresenter()
    controller = LibraryController(book_repo, reservation_repo, presenter)

    print("TEST 1: Adding books to the system")
    res1 = controller.add_book(1, "Clean Architecture", "Robert C. Martin", "COMPUTER_SCIENCE")
    print(res1)
    
    res1_double = controller.add_book(1, "Brave New World", "Aldous Huxley", "HUMANITIES")
    print(res1_double)

    print("TEST 2: Searching book by title")
    res2 = controller.search_book("Clean")
    print(res2)
    
    res2_not_found = controller.search_book("Python in Cafeteria")
    print(res2_not_found)

    print("TEST 3: Reserving an available book")
    res3 = controller.reserve_book(101, "Clean Architecture", 202611)
    print(res3)
    
    print("Trying to reserve the same book again")
    res3_fail = controller.reserve_book(102, "Clean Architecture", 202612)
    print(res3_fail)

    print("TEST 4: Listing all books to verify status")
    print(controller.list_all_books())

    print("TEST 5: Canceling the reservation")
    res5 = controller.cancel_reservation("Clean Architecture")
    print(res5)
    
    print("Verifying book status after cancellation")
    print(controller.list_all_books())

    print("TEST 6: Testing book return")
    controller.reserve_book(103, "Clean Architecture", 202611)
    print("Book reserved again for return test")
    
    res6 = controller.return_book(1)
    print(res6)
    
    print(controller.list_all_books())
    print("ALL TESTS COMPLETED")

if __name__ == "__main__":
    run_tests()