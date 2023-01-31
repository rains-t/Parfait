import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont
from PyQt5.QtWidgets import *
from PCore import *

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
        #setting color
        pal = QPalette()
        role = QPalette.Background
        pal.setColor(role, QColor(255, 251, 162))
        self.setPalette(pal)

        #widget colorscheme
        widgetPal = QPalette()
        widgetPal.setColor(role,QColor(100,99,82))
        
        #setting fixed window size
        self.setFixedSize(QSize(375,450))
        self.userLabel = QLabel('Username')
        self.userLabel.setFont(QFont('Arial',7))
        self.passLabel = QLabel('Password')
        self.passLabel.setFont(QFont('Arial',7))

        self.textName = QLineEdit()
        self.textName.setAutoFillBackground(True)
        self.textName.setBackgroundRole(QPalette.Base)
        #using this palette for all widgets
        p = self.textName.palette() 
        p.setColor(self.textName.backgroundRole(), QColor(255,253,208))
        self.textName.setPalette(p)
        self.textName.setObjectName('username')

        self.textPass = QLineEdit()
        self.textPass.setAutoFillBackground(True)
        self.textPass.setPalette(p)
        self.textPass.setObjectName('password')
        self.textPass.setEchoMode(QLineEdit.Password)

        self.logButton = QPushButton('Log In', self)
        self.logButton.setAutoFillBackground(True)
        self.logButton.setPalette(p)
        self.logButton.setFont(QFont('Arial',9))
        self.logButton.clicked.connect(self.handleLogin)

        self.createAccount = QPushButton('Sign Up')
        self.createAccount.setAutoFillBackground(True)
        self.createAccount.setPalette(p)
        self.createAccount.setFont(QFont('Arial',9))
        self.createAccount.clicked.connect(self.handleCreate)

        #main layout 
        layout = QGridLayout(self)
        
        #layout to contain the labels (username/password)
        labelLayout = QVBoxLayout()

        #layout to contain toggle for echo mode
        checkLayout = QHBoxLayout()
        #checkLayout.addWidget(QWidget())
        self.showPass = QCheckBox('&Show password')
        #self.showPass.setFont(QFont, 'Arial', 7)
        
        #allowing the checkbox to show background color whenever unchecked
        #VERY difficult code to find
        self.showPass.setStyleSheet("QCheckBox::indicator:unchecked"
                               "{"
                               "Border : 1px solid #5A5A5A ;"
                               "Background : rgb(255,253,208) ;"
                               "}")

        #self.showPass.setPalette(pal)
        self.showPass.setCheckable(True)
        self.showPass.stateChanged.connect(self.checkedBox)
        checkLayout.addWidget(self.showPass)
        #self.showpass.toggled.connect(self.textPass.setEchoMode(QLineEdit.Password))

        signLabel = QLabel('Sign in to continue')
        signLabel.setFont(QFont('Arial', 15))
        

        #layout to hold the log in information
        logLayout = QVBoxLayout()    
        logLayout.addWidget(self.textName)
        logLayout.addWidget(self.textPass)
        logLayout.setSpacing(25)

        labelLayout.addWidget(self.userLabel)
        labelLayout.addWidget(self.passLabel)
        labelLayout.setSpacing(25)

        layout.addLayout(labelLayout,2,1)
        layout.addLayout(logLayout,2,2,1,2)
        layout.addWidget(self.logButton,4,2)
        layout.addWidget(self.createAccount,4,3)
        #creating blank space with a blank QWidget
        layout.addWidget(QWidget(),1,0)
        layout.addWidget(signLabel,1,2,1,3)
        layout.addWidget(QWidget(),1,4)
        layout.addWidget(QWidget(),2,5)
        layout.addWidget(QWidget(),4,0)
        layout.addWidget(QWidget(),5,0)
        layout.addWidget(QWidget(),6,0)
        #adding checkbox to main layout
        layout.addLayout(checkLayout,3,2)
        


    


    def handleLogin(self):
        username = self.textName.text()
        password = self.textPass.text()

        if log_in(username, password) == True:
            QMessageBox.information(self, ' ', 'logging in')
            self.close()
            #send to main window if log in verified
            self.openMainWindow()

        else:
            QMessageBox.warning(self, 'Error', 'Invalid username or password')
            #in future create a counter for if username == valid and password False 4 times in a row
            #account will be locked out

    def handleCreate(self):
        #send to account creation page
        if True:
            QMessageBox.information(self,'Success','Account created')

    def checkedBox(self):
        if self.showPass.isChecked():
            self.textPass.setEchoMode(False)

        else:
            self.textPass.setEchoMode(QLineEdit.Password)

    def openMainWindow(self):
        self.close()
        self.mainApp = MainWindow()
        self.mainApp.show()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Parfait')
        self.setMinimumSize(500,500)
        widget = QWidget()
        self.setCentralWidget(widget)


        
        






        
        


def main():
    app = QApplication(sys.argv)
    window = LogWindow()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()

        




