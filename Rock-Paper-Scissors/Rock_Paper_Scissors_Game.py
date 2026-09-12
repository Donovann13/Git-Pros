
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QRadioButton,QButtonGroup
from PyQt5.QtGui import QIcon,QFont

class MyWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.HW = 0
        self.CW = 0
        self.D = 0

        import os
        from dotenv import load_dotenv
        load_dotenv()
        Icon_File = os.getenv("Icon_File")

        self.setWindowTitle("Rock Paper Scissors Game")
        self.setGeometry(800,200,1000,600)
        self.setWindowIcon(QIcon(f"{Icon_File}"))
        self.setStyleSheet("background-color: #C2E7D9;")

        self.label1 = QLabel("Welcome to the Rock Paper Scissors Game!",self)
        self.label1.setGeometry(15,10,600,50)
        self.label1.setFont(QFont("Impact",15))

        self.button1 = QPushButton("Start Game",self)
        self.button1.setGeometry(470,15,150,40)
        self.button1.setFont(QFont("Impact",12))
        self.button1.setStyleSheet("background-color:#A6CFD5;")

        self.label3 = QLabel("🪨📄✂️",self)
        self.label3.setGeometry(830,10,200,50)
        self.label3.setFont(QFont("Impact",25))

        self.label2 = QLabel("Game started! Choose your option:",self)
        self.label2.setGeometry(15,10,600,50)
        self.label2.setFont(QFont("Impact",15))
        self.label2.hide()

        self.label7 = QLabel("CPU",self)
        self.label7.setGeometry(750,100,60,50)
        self.label7.setFont(QFont("Impact",15))
        self.label7.hide()

        self.label8 = QLabel("YOU",self)
        self.label8.setGeometry(250,100,60,50)
        self.label8.setFont(QFont("Impact",15))
        self.label8.hide()

        self.radio1 = QRadioButton("🪨",self)
        self.radio1.setGeometry(400,15,130,40)
        self.radio1.setFont(QFont("Impact",20))
        self.radio1.hide()

        self.radio2 = QRadioButton("📄",self)
        self.radio2.setGeometry(505,15,140,40)
        self.radio2.setFont(QFont("Impact",20))
        self.radio2.hide()
        
        self.radio3 = QRadioButton(" ✂️",self)
        self.radio3.setGeometry(605,15,150,40)
        self.radio3.setFont(QFont("Impact",20))
        self.radio3.hide()

        self.group1 = QButtonGroup(self)
        self.group1.addButton(self.radio1)
        self.group1.addButton(self.radio2)
        self.group1.addButton(self.radio3)

        self.button1.pressed.connect(self.clicked)

        self.radio1.clicked.connect(self.radio_clicked)
        self.radio2.clicked.connect(self.radio_clicked)
        self.radio3.clicked.connect(self.radio_clicked)

    def clicked(self):
        self.button1.close()
        self.label1.close()
        self.label2.show()
        self.radio1.show()
        self.radio2.show()
        self.radio3.show()

    def radio_clicked(self):

        user_option = self.sender()
        if user_option.isChecked():
            self.label2.close()
            self.label4 = QLabel(f"You chose {user_option.text()}",self)
            self.label4.setGeometry(15,10,250,32)
            self.label4.setFont(QFont("Impact",15))
            self.label4.show()

        import random
        computer_option = random.choice(["🪨","📄"," ✂️"])
        self.label5 = QLabel(f"Computer chose {computer_option}",self)
        self.label5.setGeometry(15,50,400,32)
        self.label5.setFont(QFont("Impact",15))
        self.label5.show()

        self.label7.show()
        self.label8.show()

        self.label9 = QLabel(f"{computer_option}",self)
        self.label9.setGeometry(640,150,300,300)
        self.label9.setFont(QFont("Impact",120))
        self.label9.show()

        self.label10 = QLabel(f"{user_option.text()}",self)
        self.label10.setGeometry(140,150,300,300)
        self.label10.setFont(QFont("Impact",120))
        self.label10.show()

        if user_option.text() == "🪨":
            if computer_option == "📄":
                self.CW += 1
            elif computer_option == " ✂️":
                self.HW += 1
            elif computer_option == "🪨":
                self.D += 1

        elif user_option.text() == "📄":
            if computer_option == "📄":
                self.D += 1
            elif computer_option == " ✂️":
                self.CW += 1
            elif computer_option == "🪨":
                self.HW += 1

        elif user_option.text() == " ✂️":
            if computer_option == "📄":
                self.HW += 1
            elif computer_option == " ✂️":
                self.D += 1
            elif computer_option == "🪨":
                self.CW += 1

        self.label6 = QLabel(f"Human wins:{self.HW}  Computer wins:{self.CW}  Draws:{self.D}",self)
        self.label6.setGeometry(530,530,600,50)
        self.label6.setFont(QFont("Impact",15))
        self.label6.show()

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()