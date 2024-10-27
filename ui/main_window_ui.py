
from PyQt5 import QtWidgets, QtCore

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        # Book Title input
        self.bookTitleInput = QtWidgets.QLineEdit(self.centralwidget)
        self.bookTitleInput.setGeometry(QtCore.QRect(50, 50, 200, 30))
        self.bookTitleInput.setPlaceholderText("Book Title")
        
        # Book Author input
        self.bookAuthorInput = QtWidgets.QLineEdit(self.centralwidget)
        self.bookAuthorInput.setGeometry(QtCore.QRect(50, 90, 200, 30))
        self.bookAuthorInput.setPlaceholderText("Book Author")
        
        # Add Book button
        self.addBookButton = QtWidgets.QPushButton(self.centralwidget)
        self.addBookButton.setGeometry(QtCore.QRect(50, 130, 100, 30))
        self.addBookButton.setText("Add Book")

        # Books list display
        self.booksListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.booksListWidget.setGeometry(QtCore.QRect(300, 50, 250, 150))
        
        # View Books button
        self.viewBooksButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewBooksButton.setGeometry(QtCore.QRect(50, 170, 100, 30))
        self.viewBooksButton.setText("View Books")

        # Review input
        self.bookIDInput = QtWidgets.QLineEdit(self.centralwidget)
        self.bookIDInput.setGeometry(QtCore.QRect(50, 220, 100, 30))
        self.bookIDInput.setPlaceholderText("Book ID")
        
        self.reviewTextInput = QtWidgets.QLineEdit(self.centralwidget)
        self.reviewTextInput.setGeometry(QtCore.QRect(50, 260, 200, 30))
        self.reviewTextInput.setPlaceholderText("Review Text")
        
        self.ratingInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ratingInput.setGeometry(QtCore.QRect(50, 300, 100, 30))
        self.ratingInput.setPlaceholderText("Rating")

        # Add Review button
        self.addReviewButton = QtWidgets.QPushButton(self.centralwidget)
        self.addReviewButton.setGeometry(QtCore.QRect(50, 340, 100, 30))
        self.addReviewButton.setText("Add Review")

        # Reviews list display
        self.reviewsListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.reviewsListWidget.setGeometry(QtCore.QRect(300, 220, 250, 150))

        # View Reviews button
        self.viewReviewsButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewReviewsButton.setGeometry(QtCore.QRect(50, 380, 100, 30))
        self.viewReviewsButton.setText("View Reviews")

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Book Exchange - Main")
