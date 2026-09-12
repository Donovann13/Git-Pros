import sys
import random
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton,QLabel,QLineEdit,QRadioButton,QButtonGroup,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QIcon,QFont,QPixmap

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        import os
        from dotenv import load_dotenv
        load_dotenv()
        Icon_File = os.getenv("Icon_File")

        self.setWindowIcon(QIcon(f"{Icon_File}"))
        self.setWindowTitle("Slot Machine")
        self.setGeometry(880,130,900,620)
        self.initUI()

    def initUI(self):

        self.balance = 100

        self.label1 = QLabel("Welcome to Slot Machine!",self)
        self.label1.setGeometry(295,10,350,50)
        self.label1.setFont(QFont("Impact",15))
        self.label1.show()

        self.button1 = QPushButton("Start",self)
        self.button1.setGeometry(380,200,150,90)
        self.button1.setFont(QFont("Impact",15))

        self.button2 = QPushButton("Click to Roll",self)
        self.button2.setGeometry(380,500,150,90)
        self.button2.setFont(QFont("Impact",15))
        self.button2.hide()

        self.button1.pressed.connect(self.button1pressed)
        self.button2.pressed.connect(self.button2pressed)
        
    def button1pressed(self):

        self.button2.show()
        self.label1.close()
        self.button1.close()

        self.label2 = QLabel(f"Balance: ${self.balance}",self)
        self.label2.setGeometry(15,10,250,50)
        self.label2.setFont(QFont("Impact",15))
        self.label2.show()

        self.label3 = QLabel("Error: invalid input or insufficient balance!",self)
        self.label3.setGeometry(15,60,500,50)
        self.label3.setFont(QFont("Impact",15))
        self.label3.hide()

        self.label5 = QLabel(self)
        self.label5.setGeometry(330,295,500,100)
        self.label5.setFont(QFont("Impact",30))

        self.label6 = QLabel("Game Over!",self)
        self.label6.setGeometry(295,290,350,100)
        self.label6.setFont(QFont("Impact",40))
        
        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setGeometry(325,440,250,50)
        self.lineedit1.setPlaceholderText("Enter bet amount...")
        self.lineedit1.setFont(QFont("Impact",15))
        self.lineedit1.show()

        self.label7 = QLabel(self)
        self.label7.setGeometry(170,105,200,200)

        self.label8 = QLabel(self)
        self.label8.setGeometry(370,105,200,200)

        self.label9 = QLabel(self)
        self.label9.setGeometry(570,105,200,200)

    def button2pressed(self):

        if self.balance == 0:
            self.label6.show()

        import os
        from dotenv import load_dotenv
        load_dotenv()
        choice1_File = os.getenv("choice1_File")
        choice2_File = os.getenv("choice2_File")
        choice3_File = os.getenv("choice3_File")

        choose_list = [choice1_File,choice2_File,choice3_File]

        self.x1 = 2
        self.x2 = 3
        self.x3 = 5
            
        if self.lineedit1.text() and self.lineedit1.text().isdigit() and int(self.lineedit1.text()) <= self.balance and int(self.lineedit1.text()) > 0:

            self.label3.hide()

            self.choice1 = random.choice(choose_list)
            self.label7.setPixmap(QPixmap(f"{self.choice1}"))
            self.label7.show()

            self.choice2 = random.choice(choose_list)
            self.label8.setPixmap(QPixmap(f"{self.choice2}"))
            self.label8.show()

            self.choice3 = random.choice(choose_list)
            self.label9.setPixmap(QPixmap(f"{self.choice3}"))
            self.label9.show()

            self.bet = int(self.lineedit1.text())
            self.balance -= self.bet
            self.label2.setText(f"Balance: ${self.balance}")

            self.label5.hide()

            if self.choice1 == self.choice2 == self.choice3 == choice1_File:

                self.payout = self.bet * self.x1
                self.label5.setText(f"You won ${self.payout}")
                self.label5.show()

            elif self.choice1 == self.choice2 == self.choice3 == choice2_File:

                self.payout = self.bet * self.x2
                self.label5.setText(f"You won ${self.payout}")
                self.label5.show()

            elif self.choice1 == self.choice2 == self.choice3 == choice3_File:

                self.payout = self.bet * self.x3
                self.label5.setText(f"You won ${self.payout}")
                self.label5.show()

            else:
                self.payout = 0

            self.balance += self.payout
            self.label2.setText(f"Balance: ${self.balance}")

        else:
            self.label3.show()

def main():

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()