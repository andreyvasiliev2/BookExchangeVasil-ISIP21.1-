import pytest
from database import connect_to_db, register_user, authenticate_user, add_book, get_books, add_review, get_reviews

@pytest.fixture
def db_connection():
    conn = connect_to_db()
    yield conn
    conn.close()

def test_register_user(db_connection):
    # Test registering a new user
    result = register_user(db_connection, "test_user", "test_password")
    assert result is True

def test_authenticate_user(db_connection):
    # Test authenticating a registered user
    register_user(db_connection, "auth_user", "auth_password")
    result = authenticate_user(db_connection, "auth_user", "auth_password")
    assert result is True

def test_add_book(db_connection):
    # Test adding a new book
    result = add_book(db_connection, "Test Book", "Test Author")
    assert result is True

def test_get_books(db_connection):
    # Test retrieving a list of books
    add_book(db_connection, "Sample Book", "Sample Author")
    books = get_books(db_connection)
    assert len(books) > 0

def test_add_review(db_connection):
    # Test adding a review for an existing book
    add_book(db_connection, "Review Book", "Review Author")
    books = get_books(db_connection)
    book_id = books[-1]['book_id']
    result = add_review(db_connection, book_id, "Great book!", 5)
    assert result is True

def test_get_reviews(db_connection):
    # Test retrieving reviews for a specific book
    add_book(db_connection, "Book with Reviews", "Author")
    books = get_books(db_connection)
    book_id = books[-1]['book_id']
    add_review(db_connection, book_id, "Interesting read", 4)
    reviews = get_reviews(db_connection)
    assert len(reviews) > 0
