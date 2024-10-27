
import pyodbc

def connect_to_db():
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=BookExchangeDB;Trusted_Connection=yes')
    return conn

def authenticate_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE Username = ? AND Password = ?", (username, password))
    return cursor.fetchone() is not None

def register_user(conn, username, password):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Users (Username, Password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except pyodbc.IntegrityError as e:
        print(f"Error during registration: {e}")
        return False
    finally:
        cursor.close()


def add_book(conn, title, author):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Books (Title, Author) VALUES (?, ?)",
                       (title, author))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error adding book: {e}")
        return False
    finally:
        cursor.close()

def get_books(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    books = [{'title': row.Title, 'author': row.Author} for row in cursor.fetchall()]
    cursor.close()
    return books


def add_review(conn, book_id, review_text, rating):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Reviews (BookID, ReviewText, Rating) VALUES (?, ?, ?)",
                       (book_id, review_text, rating))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error adding review: {e}")
        return False
    finally:
        cursor.close()

def get_reviews(conn, book_id):
    cursor = conn.cursor()
    cursor.execute("SELECT ReviewText, Rating FROM Reviews WHERE BookID = ?", (book_id,))
    reviews = [{'text': row.ReviewText, 'rating': row.Rating} for row in cursor.fetchall()]
    cursor.close()
    return reviews
