from flask import Blueprint, jsonify, request
from services.Service import get_all_books_service, get_book_by_id_service, create_book_service, delete_book_service

books_bp = Blueprint('books', __name__)

@books_bp.route('/api/books', methods=['GET'])
def get_books_route():    
    return (get_all_books_service())

@books_bp.route('/api/books', methods=['POST'])
def create_book_route():
    data = request.get_json()
    title = data.get('title')
    price_in_pence = data.get('price_in_pence')
    quantity_in_stock = data.get('quantity_in_stock')
    release_date = data.get('release_date')
    is_fiction = data.get('is_fiction')

    if not title or not price_in_pence or not quantity_in_stock or not release_date or not is_fiction:
        return jsonify({'error': 'bad request'}), 400
    
    new_book = create_book_service(title, price_in_pence, quantity_in_stock, release_date, is_fiction)
    return jsonify({'message': 'book created successfully', 'new_book': new_book})

@books_bp.route('/api/books/<int:book_id>', methods=['GET'])
def get_book_by_id_route(book_id):
    book = get_book_by_id_service(book_id)
    if book:
        return jsonify({'book': {'book_id': book.book_id, 'title': book.title, 'price_in_pence': book.price_in_pence, 'quantity_in_stock': book.quantity_in_stock, 'is_fiction': book.is_fiction}})
    else: 
        return jsonify({'error': 'Book not found'}), 404

@books_bp.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book_route(book_id):
    existing_book = get_book_by_id_service(book_id)
    if existing_book:
        delete_book_service(book_id)
        return jsonify({'message': 'book deleted successfully'}), 200
    else: 
        return jsonify({'error': 'book not found'}), 404   