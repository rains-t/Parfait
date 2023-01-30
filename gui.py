import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtWidgets import *
from main import *

class Color(QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class LogWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Log in')
        #setting fixed window size
        self.setFixedSize(QSize(350,450))
        self.userLabel = QLabel('Username')
        self.passLabel = QLabel('Password')
        self.textName = QLineEdit()
        self.textName.setObjectName('username')
        self.textPass = QLineEdit()
        self.textPass.setObjectName('password')
        self.textPass.setEchoMode(QLineEdit.Password)
        self.logButton = QPushButton('Log in', self)
        self.logButton.clicked.connect(self.handleLogin)
        self.createAccount = QPushButton('Create Account')
        self.createAccount.clicked.connect(self.handleCreate)
        #main layout 
        layout = QGridLayout(self)
        
        #layout to contain the labels (username/password)
        labelLayout = QVBoxLayout()

        #layout to hold the log in information
        logLayout = QVBoxLayout()    
        logLayout.addWidget(self.textName)
        logLayout.addWidget(self.textPass)
        logLayout.setSpacing(25)

        labelLayout.addWidget(self.userLabel)
        labelLayout.addWidget(self.passLabel)
        labelLayout.setSpacing(25)

        layout.addLayout(labelLayout,1,0)
        layout.addLayout(logLayout,1,1,1,2)
        layout.addWidget(self.logButton,2,1)
        layout.addWidget(self.createAccount,2,2)
        #creating blank space with a blank QWidget
        layout.addWidget(QWidget(),1,3)
        #This is to add a QCheckBox later to allow echomode to be set to off for password if desired
        #self.textPass.setEchoMode(False)

        

        

        







    def handleLogin(self):
        username = self.textName.text()
        password = self.textPass.text()

        if log_in(username, password) == True:
            QMessageBox.information(self, ' ', 'logging in')
            #send to main window
        else:
            QMessageBox.warning(self, 'Error', 'Invalid username or password')
            #in future create a counter for if username == valid and password False 4 times in a row
            #account will be locked out

    def handleCreate(self):
        #send to account creation page
        if True:
            QMessageBox.information(self,' ','Account created')

        
        






        
        



        


app = QApplication(sys.argv)
window = LogWindow()
window.show()
app.exec()


