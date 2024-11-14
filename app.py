import psycopg2
import psycopg2.extras
from flask import Flask, jsonify


app = Flask(__name__) 

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='my_bookshop')
    return conn

@app.route('/')
def json():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    
    books_list = [dict(book) for book in books]
    
    return jsonify(books_list)