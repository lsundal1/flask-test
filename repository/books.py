import psycopg2.extras
from flask import jsonify
from models.books import Book

def db_conn():
    conn = psycopg2.connect(host='localhost', database='my_bookshop')
    return conn

def get_all_books():
    conn = db_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('''SELECT * FROM books''')
    books = cur.fetchall()
    cur.close()
    conn.close()
    
    books_list = [dict(book) for book in books]
    
    return jsonify(books_list)

def get_book_by_id(book_id):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM books WHERE book_id = %s''', (book_id,))
    book_data = cur.fetchone()
    cur.close()
    conn.close()

    if book_data:
        return Book(author_id=book_data[0], book_id=book_data[1], is_fiction=book_data[2], price_in_pence=book_data[3], quantity_in_stock=book_data[4], release_date=book_data[5], title=book_data[6])
		
    else:
        return None

def create_book(title, price_in_pence, quantity_in_stock, release_date, is_fiction):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''INSERT INTO books (title, price_in_pence, quantity_in_stock, release_date, is_fiction) VALUES(%s, %s, %s, %s, %s) RETURNING *''', (title, price_in_pence, quantity_in_stock, release_date, is_fiction))
    new_book_data = cur.fetchone()
    conn.commit()

    new_book = {
        "book_id": new_book_data[0],
        "title": new_book_data[1],
        "price_in_pence": new_book_data[2],
        "quantity_in_stock": new_book_data[3],
        "release_date": new_book_data[4],
        "is_fiction": new_book_data[5],
        "author_id": new_book_data[6],
    }

    cur.close()
    conn.close()

    return new_book

def delete_book(book_id):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''DELETE FROM books WHERE book_id = %s''', (book_id,))
    conn.commit()
    cur.close()
    conn.close()

