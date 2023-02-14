import sys
from PyQt5.QtCore import Qt, QSize, pyqtSignal, QObject
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
    #identity = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('Parfait')

        #setting color
        pal = QPalette()
        role = QPalette.Background
        pal.setColor(role, QColor(255, 251, 162))
        self.setPalette(pal)
        
        

        
        #setting fixed window size
        self.setFixedSize(QSize(375,450))

        self.userLabel = QLabel('Username')
        self.userLabel.setFont(QFont('Arial',7))

        self.passLabel = QLabel('Password')
        self.passLabel.setFont(QFont('Arial',7))


        self.textName = QLineEdit()
        self.textName.setAutoFillBackground(True)
        self.textName.setStyleSheet("QLineEdit"
                               "{"
                               "Border : 1px solid #adadad ;"
                               "Background : rgb(255,253,208) ;"
                               "}"
                               "QLineEdit:hover"
                               "{"
                               "Border : 1px solid #637bff ;"
                               "Background : #dfe5e8 ;"                            
                               "}")

        self.textName.setObjectName('username')
        self.textPass = QLineEdit()
        self.textPass.setAutoFillBackground(True)
        self.textPass.setStyleSheet("QLineEdit"
                               "{"
                               "Border : 1px solid #adadad ;"
                               "Background : rgb(255,253,208) ;"
                               "}"
                               "QLineEdit:hover"
                               "{"
                               "Border : 1px solid #637bff ;"
                               "Background : #dfe5e8 ;"                            
                               "}")
        self.textPass.setObjectName('password')
        self.textPass.setEchoMode(QLineEdit.Password)


        self.logButton = QPushButton('Log In', self)
        self.logButton.setAutoFillBackground(True)
        self.logButton.setStyleSheet("QPushButton"
                               "{"
                               
                               "Border : 1px solid #adadad ;"
                               "Background : rgb(255,253,208) ;"
                               "border-radius: 10px;"
                               "padding : 4px;"
                               "border-style : outset "

                               "}"
                               "QPushButton:hover:!pressed"
                               "{"
                               "Border : 1px solid #637bff ;"
                               "Background : #dfe5e8 ;"                               
                               "}")
        self.logButton.setFont(QFont('Arial',9))
        self.logButton.clicked.connect(self.handleLogin)

        self.createAccount = QPushButton('Sign Up')
        self.createAccount.setAutoFillBackground(True)
        self.createAccount.setStyleSheet("QPushButton"
                               "{"
                               
                               "Border : 1px solid #adadad ;"
                               "Background : rgb(255,253,208) ;"
                               "border-radius: 10px;"
                               "padding : 4px;"
                               "border-style : outset;"
                               "min-width : 100px;"

                               "}"
                               "QPushButton:hover:!pressed"
                               "{"
                               "Border : 1px solid #637bff ;"
                               "Background : #dfe5e8 ;"                            
                               "}")
        self.createAccount.setFont(QFont('Arial',9))
        self.createAccount.clicked.connect(self.handleCreate)

        #main layout 
        layout = QGridLayout(self)
        
        #layout to contain the labels (username/password)
        labelLayout = QVBoxLayout()

        #layout to contain toggle for echo mode
        checkLayout = QHBoxLayout()

        self.showPass = QCheckBox('&Show password')

        
        #allowing the checkbox to show background color whenever unchecked
        #VERY difficult code to find
        self.showPass.setStyleSheet("QCheckBox::indicator:unchecked"
                               "{"
                               "Border : 1px solid #adadad ;"
                               "Background : rgb(255,253,208) ;"
                               "}"
                               "QCheckBox::indicator:hover:unchecked"
                               "{"
                               "Border : 1px solid #637bff ;"
                               "Background : #dfe5e8 ;"                            
                               "}")

        #self.showPass.setPalette(pal)
        self.showPass.setCheckable(True)
        self.showPass.stateChanged.connect(self.checkedBox)
        checkLayout.addWidget(self.showPass)

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
        

        if sql_controls().log_in(username, password) == True:
            #QMessageBox.information(self, ' ', 'logging in')
            #self.identitySignal(username)
            self.closeAndReturn()

            #send to main window if log in verified
            #self.openMainWindow()

        else:
            QMessageBox.warning(self, 'Error', 'Invalid username or password')
            #in future create a counter for if username == valid and password False 4 times in a row
            #account will be locked out

    def identitySignal(self,user):
        self.identity.emit(user)

    def testTrigger(self):
        print('signal sent')


    def handleCreate(self):
        #send to account creation page
        #self.hide()
        self.openAccountCreationPage()

    def checkedBox(self):
        if self.showPass.isChecked():
            self.textPass.setEchoMode(False)

        else:
            self.textPass.setEchoMode(QLineEdit.Password)

    # def openMainWindow(self):
    #     self.close()
    #     self.mainApp = MainWindow()
    #     self.mainApp.show()
    def closeAndReturn(self):
        self.deleteLater()
        self.close()
        self.parent().show()

    def openAccountCreationPage(self):
        # self.accCreation = AccountCreationPage()
        # self.accCreation.show()
        self.accCreation = AccountCreationPage(self)
        self.hide()
        self.accCreation.show()




class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Parfait')
        self.setMinimumSize(500,500)
        self.login()
        self.widget = QLabel()
        self.setCentralWidget(self.widget)



    def login(self):
        self.logPage = LogWindow(self)
        self.logPage.show()

        self.logPage.logButton.clicked.connect(self.getIdentity)
        

    def getIdentity(self):
        self.identity = self.logPage.textName.text()
        #text = self.logPage.textName.text()
        print(self.identity)
        self.widget.setText(self.identity)

        


class AccountCreationPage(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('Parfait')

        #setting bg color
        pal = QPalette()
        role = QPalette.Background
        pal.setColor(role, QColor(255, 251, 162))
        self.setPalette(pal)
   
        #setting fixed window size
        self.setFixedSize(QSize(375,450))
        layout = QGridLayout()
        labelLayout = QVBoxLayout()
        textLayout = QVBoxLayout()


        self.setLayout(layout)

        self.userEmailLabel = QLabel('Email')
        self.userEmailLabel.setFont(QFont('Arial',9))

        self.userLabel = QLabel('Username')
        self.userLabel.setFont(QFont('Arial',9))

        self.passLabel = QLabel('Password')
        self.passLabel.setFont(QFont('Arial', 9))

        self.retypePassLabel = QLabel('Retype password')
        self.retypePassLabel.setFont(QFont('Arial', 9))

        pageLabel = QLabel('Create an account')
        pageLabel.setFont(QFont('Arial', 15))

        self.userEmail = QLineEdit()
        self.userEmail.setFont(QFont('Arial', 9))
        self.userEmail.setAutoFillBackground(True)
        self.userEmail.setStyleSheet("QLineEdit"
                               "{"
                               "Border : 1px solid #adadad ;"
                               "Background : rgb(255,253,208) ;"
                               "}"
                               "QLineEdit:hover"
                               "{"
                               "Border : 1px solid #637bff ;"
                               "Background : #dfe5e8 ;"                            
                               "}")

        self.userEmail.setObjectName('email')


        self.userName = QLineEdit()
        self.userName.setFont(QFont('Arial', 9))
        self.userName.setAutoFillBackground(True)
        self.userName.setStyleSheet("QLineEdit"
                               "{"
                               "Border : 1px solid #adadad ;"
                               "Background : rgb(255,253,208) ;"
                               "}"
                               "QLineEdit:hover"
                               "{"
                               "Border : 1px solid #637bff ;"
                               "Background : #dfe5e8 ;"                            
                               "}")

        self.userName.setObjectName('username')

        self.userPass = QLineEdit()
        self.userPass.setEchoMode(QLineEdit.Password)
        self.userPass.setAutoFillBackground(True)
        self.userPass.setStyleSheet("QLineEdit"
                               "{"
                               "Border : 1px solid #adadad ;"
                               "Background : rgb(255,253,208) ;"
                               "}"
                               "QLineEdit:hover"
                               "{"
                               "Border : 1px solid #637bff ;"
                               "Background : #dfe5e8 ;"                            
                               "}")

        self.retypeUserPass = QLineEdit()
        self.retypeUserPass.setEchoMode(QLineEdit.Password)
        self.retypeUserPass.setAutoFillBackground(True)
        self.retypeUserPass.setStyleSheet("QLineEdit"
                               "{"
                               "Border : 1px solid #adadad ;"
                               "Background : rgb(255,253,208) ;"
                               "}"
                               "QLineEdit:hover"
                               "{"
                               "Border : 1px solid #637bff ;"
                               "Background : #dfe5e8 ;"                            
                               "}")

        self.createAccButton = QPushButton('Create Account')
        self.createAccButton.setAutoFillBackground(True)
        self.createAccButton.setStyleSheet("QPushButton"
                               "{"
                               
                               "Border : 1px solid #adadad ;"
                               "Background : rgb(255,253,208) ;"
                               "border-radius: 10px;"
                               "padding : 4px;"
                               "border-style : outset;"
                               "max-width : 200px;"

                               "}"
                               "QPushButton:hover:!pressed"
                               "{"
                               "Border : 1px solid #637bff ;"
                               "Background : #dfe5e8 ;"                            
                               "}")
        self.createAccButton.clicked.connect(self.handleCreate)

        self.pageBackButton = QPushButton('Back to Log In')
        self.pageBackButton.setAutoFillBackground(True)
        self.pageBackButton.setStyleSheet("QPushButton"
                               "{"
                               
                               "Border : 1px solid #adadad ;"
                               "Background : rgb(255,253,208) ;"
                               "border-radius: 10px;"
                               "padding : 4px;"
                               "border-style : outset;"
                               "max-width : 200px;"

                               "}"
                               "QPushButton:hover:!pressed"
                               "{"
                               "Border : 1px solid #637bff ;"
                               "Background : #dfe5e8 ;"                            
                               "}")

        self.pageBackButton.clicked.connect(self.closeAndReturn)
        

        labelLayout.addWidget(self.userEmailLabel)
        labelLayout.addWidget(self.userLabel)
        labelLayout.addWidget(self.passLabel)
        labelLayout.addWidget(self.retypePassLabel)

        textLayout.addWidget(self.userEmail)
        textLayout.addWidget(self.userName)
        textLayout.addWidget(self.userPass)
        textLayout.addWidget(self.retypeUserPass)

        #adding free space to grid layout
        layout.addLayout(labelLayout,1,1,1,1)
        layout.addLayout(textLayout,1,2,1,2)
        layout.addWidget(QWidget(),1,5)
        layout.addWidget(QWidget(),1,5)
        layout.addWidget(QWidget(),1,0)
        layout.addWidget(QWidget(),4,0)
        layout.addWidget(QWidget(),5,0)
        layout.addWidget(self.createAccButton, 3,1,1,3)
        layout.addWidget(self.pageBackButton,4,1,1,3)
        layout.addWidget(pageLabel,0,1,1,3)

    def handleCreate(self):
        email = self.userEmail.text()
        username = self.userName.text()
        password = self.userPass.text()
        retyped_password = self.retypeUserPass.text()


        if sql_controls().email_taken(email):
            QMessageBox.warning(self,'Error', 'Email already in use.')
            self.userEmail.clear()
            self.userName.clear()
            self.userPass.clear()
            self.retypeUserPass.clear()
            return       
        
        if not validate_username(username):
            (QMessageBox.warning(self, 'Error', 
            'Invalid username: username must be between 3 and 10 characters, and contain no spaces or special characters.'))
            return

        if sql_controls().username_taken(username):
            QMessageBox.warning(self,'Error','Username is already taken.')
            self.userName.clear()
            self.userPass.clear()
            self.retypeUserPass.clear()
            return
            

        if not create_password(password):
            QMessageBox.warning(self,'Error','Password must have at least: 8 digits, contain one uppercase letter, one lowercase letter, and one symbol')
            self.userPass.clear()
            self.retypeUserPass.clear()
            return

        if not retype_password(password,retyped_password):
            QMessageBox.warning(self,'Error', 'Passwords did not match.')
            self.userPass.clear()
            self.retypeUserPass.clear()

            return


        if sql_controls().create_account(email, username, password) == False:
            QMessageBox.warning(self,'Error','Something went wrong. Error code: 100')
            self.userEmail.clear()
            self.userName.clear()
            self.userPass.clear()
            self.retypeUserPass.clear()
            return

        else:
            QMessageBox.information(self,'Success', 'Account created!')
            self.userName.clear()
            self.userPass.clear()
            self.retypeUserPass.clear()
            self.closeAndReturn()
            # self.close()
            # self.openLoginPage()

    def closeAndReturn(self):
        self.deleteLater()
        self.close()
        self.parent().show()


                                            
    






        
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.hide()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()

        




