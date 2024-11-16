from flask import Flask
from routes.BooksRoutes import books_bp


app = Flask(__name__) 
app.register_blueprint(books_bp)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
