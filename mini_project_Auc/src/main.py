from src.entities.book import Category
from src.adapters.in_memory_book_repository import InMemoryBookRepository
from src.adapters.in_memory_reservation_repository import InMemoryReservationRepository

from src.use_cases.add_book import AddBookUseCase
from src.use_cases.list_books import ListBooksUseCase
from src.use_cases.reserve_book import ReserveBookUseCase
from src.use_cases.cancel_reservation import CancelReservationUseCase

from src.adapters.presenters.book_presenter import BookPresenter
from src.adapters.presenters.reservation_presenter import ReservationPresenter
from src.adapters.controllers.library_controller import LibraryController

def run_simulation():
    # 1. Repositories
    book_repo = InMemoryBookRepository()
    reservation_repo = InMemoryReservationRepository()

    # 2. Use Cases
    add_book_use_case = AddBookUseCase(book_repo)
    list_books_use_case = ListBooksUseCase(book_repo)
    reserve_book_use_case = ReserveBookUseCase(book_repo, reservation_repo)
    cancel_res_use_case = CancelReservationUseCase(reservation_repo, book_repo)

    # 3. Presenters
    book_presenter = BookPresenter()
    res_presenter = ReservationPresenter()

    # 4. Controller (Receives Use Cases and Presenters)
    controller = LibraryController(
        add_book_uc=add_book_use_case,
        list_books_uc=list_books_use_case,
        reserve_book_uc=reserve_book_use_case,
        cancel_res_uc=cancel_res_use_case,
        book_presenter=book_presenter,
        res_presenter=res_presenter
    )

    print("--- 1. ADDING BOOKS ---")
    res1 = controller.add_new_book(title="Introduction to Algorithms", author="CLRS", category=Category.COMPUTER_SCIENCE)
    res2 = controller.add_new_book(title="Clean Architecture", author="Robert C. Martin", category=Category.COMPUTER_SCIENCE)
    print(res1)
    print(res2)

    print("\n--- 2. LISTING ALL BOOKS ---")
    print(controller.show_all_books())

    # Retrieve the ID of the first added book for reservation simulation
    b1_id = book_repo.list_all()[0].id

    print("--- 3. RESERVING A BOOK ---")
    res_msg = controller.reserve_book_for_student(book_id=b1_id, user_id=101)
    print(res_msg)

    print("\n--- 4. TRYING TO RESERVE THE SAME BOOK AGAIN (Should fail) ---")
    bad_res_msg = controller.reserve_book_for_student(book_id=b1_id, user_id=102)
    print(bad_res_msg)

    print("\n--- 5. LISTING ALL BOOKS AGAIN (To verify updated status) ---")
    print(controller.show_all_books())

    # Retrieve the reservation ID to perform cancellation simulation
    res_id = list(reservation_repo._reservations.keys())[0]

    print("--- 6. CANCELLING RESERVATION ---")
    cancel_msg = controller.cancel_student_reservation(reservation_id=res_id)
    print(cancel_msg)

    print("\n--- 7. FINAL BOOKS LIST (Book should be AVAILABLE again) ---")
    print(controller.show_all_books())

if __name__ == "__main__":
    run_simulation()