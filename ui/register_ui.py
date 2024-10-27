from PyQt5 import QtWidgets, QtCore

class Ui_RegisterWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("RegisterWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        

        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(100, 80, 200, 30))
        self.usernameInput.setPlaceholderText("Username")
        

        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(100, 120, 200, 30))
        self.passwordInput.setPlaceholderText("Password")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        

        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(100, 160, 200, 30))
        self.submitButton.setText("Submit")
        
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Register")
