
from PyQt5 import QtWidgets
from ui.login_ui import Ui_LoginWindow
from ui.register_ui import Ui_RegisterWindow
from ui.main_app_ui import Ui_MainAppWindow
import database
import sys

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)


        self.setWindowTitle("Васильев Андрей ИСИП 21.1 - Вход")


        self.ui.loginButton.clicked.connect(self.handle_login)
        self.ui.registerButton.clicked.connect(self.show_registration)


        self.conn = database.connect_to_db()

    def handle_login(self):
        username = self.ui.usernameInput.text()
        password = self.ui.passwordInput.text()

        if database.authenticate_user(self.conn, username, password):
            QtWidgets.QMessageBox.information(self, 'Успех', 'Вход выполнен успешно!')
            self.show_main_app_window()
        else:
            QtWidgets.QMessageBox.warning(self, 'Ошибка входа', 'Неверное имя пользователя или пароль')

    def show_registration(self):
        self.registration_window = RegisterWindow()
        self.registration_window.show()

    def show_main_app_window(self):
        self.main_app_window = MainAppWindow(self.conn)
        self.main_app_window.show()
        self.close()

class RegisterWindow(QtWidgets.QMainWindow, Ui_RegisterWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)


        self.setWindowTitle("Васильев Андрей ИСИП 21.1 - Регистрация")
        
        self.ui.submitButton.clicked.connect(self.handle_registration)

    def handle_registration(self):
        username = self.ui.usernameInput.text()
        password = self.ui.passwordInput.text()

        if database.register_user(self.conn, username, password):
            QtWidgets.QMessageBox.information(self, 'Успех', 'Регистрация прошла успешно!')
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Регистрация не удалась. Имя пользователя уже занято.')

class MainAppWindow(QtWidgets.QMainWindow, Ui_MainAppWindow):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.ui = Ui_MainAppWindow()
        self.ui.setupUi(self)


        self.setWindowTitle("Васильев Андрей ИСИП 21.1 - Обмен книгами")


        self.ui.addBookButton.clicked.connect(self.add_book)
        self.ui.viewBooksButton.clicked.connect(self.view_books)
        self.ui.addReviewButton.clicked.connect(self.add_review)
        self.ui.viewReviewsButton.clicked.connect(self.view_reviews)

    def add_book(self):
        title = self.ui.bookTitleInput.text()
        author = self.ui.bookAuthorInput.text()
        if database.add_book(self.conn, title, author):
            QtWidgets.QMessageBox.information(self, 'Успех', 'Книга успешно добавлена!')
            self.ui.bookTitleInput.clear()
            self.ui.bookAuthorInput.clear()
        else:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Не удалось добавить книгу.')

    def view_books(self):
        books = database.get_books(self.conn)
        self.ui.booksListWidget.clear()
        for book in books:
            self.ui.booksListWidget.addItem(f"Название: {book['title']}, Автор: {book['author']}")

    def add_review(self):
        try:
            book_id = int(self.ui.bookIDInput.text())
            review_text = self.ui.reviewTextInput.text()
            rating = int(self.ui.ratingInput.text())
            if database.add_review(self.conn, book_id, review_text, rating):
                QtWidgets.QMessageBox.information(self, 'Успех', 'Отзыв успешно добавлен!')
                self.ui.reviewTextInput.clear()
                self.ui.ratingInput.clear()
            else:
                QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Не удалось добавить отзыв.')
        except ValueError:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите допустимые данные для ID книги и рейтинга.')

    def view_reviews(self):
        try:
            book_id = int(self.ui.bookIDInput.text())
            reviews = database.get_reviews(self.conn, book_id)
            self.ui.reviewsListWidget.clear()
            for review in reviews:
                self.ui.reviewsListWidget.addItem(f"Отзыв: {review['text']}, Рейтинг: {review['rating']}")
        except ValueError:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите допустимый ID книги.')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
