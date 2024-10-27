from PyQt5 import QtWidgets, QtCore

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("LoginWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        

        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(100, 80, 200, 30))
        self.usernameInput.setPlaceholderText("Username")
        

        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(100, 120, 200, 30))
        self.passwordInput.setPlaceholderText("Password")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        

        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(100, 160, 200, 30))
        self.loginButton.setText("Login")
        

        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(100, 200, 200, 30))
        self.registerButton.setText("Register")
        
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Login")
