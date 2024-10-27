
from PyQt5 import QtWidgets, QtCore

class Ui_BookWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("BookWindow")
        MainWindow.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # Book list
        self.bookList = QtWidgets.QListWidget(self.centralwidget)
        self.bookList.setGeometry(QtCore.QRect(50, 50, 300, 200))

        # Title and Author inputs
        self.titleInput = QtWidgets.QLineEdit(self.centralwidget)
        self.titleInput.setGeometry(QtCore.QRect(50, 300, 300, 30))
        self.titleInput.setPlaceholderText("Enter book title")

        self.authorInput = QtWidgets.QLineEdit(self.centralwidget)
        self.authorInput.setGeometry(QtCore.QRect(50, 350, 300, 30))
        self.authorInput.setPlaceholderText("Enter author")

        # Buttons
        self.addBookButton = QtWidgets.QPushButton(self.centralwidget)
        self.addBookButton.setGeometry(QtCore.QRect(50, 400, 300, 30))
        self.addBookButton.setText("Add Book")

        self.viewReviewsButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewReviewsButton.setGeometry(QtCore.QRect(50, 450, 300, 30))
        self.viewReviewsButton.setText("View Reviews")

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Book Management")
