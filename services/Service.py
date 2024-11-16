from repository.books import get_all_books, get_book_by_id, create_book

def get_all_books_service():
    return get_all_books()

def get_book_by_id_service(book_id):
    return get_book_by_id(book_id)

def create_book_service(title, price_in_pence, quantity_in_stock, release_date, is_fiction):
    return create_book(title, price_in_pence, quantity_in_stock, release_date, is_fiction)