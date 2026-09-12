import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,QVBoxLayout,QLabel
from PyQt5.QtCore import QTimer,Qt
from PyQt5.QtGui import QPixmap,QPainter,QIcon

class Rimspin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rim Spin")

        import os
        from dotenv import load_dotenv
        load_dotenv()
        Icon_File = os.getenv("Icon_File")
        self.Rim_Pic_File = os.getenv("Pic_File")
        self.setWindowIcon(QIcon(f"{Icon_File}"))
        self.setGeometry(1000, 130, 600, 900)

        self.angle = 0

        self.label = QLabel("Enter RPM Below")
        self.label.setStyleSheet("font-size: 15px; font-family: Arial;")
        self.label.setAlignment(Qt.AlignCenter)

        self.inputline = QLineEdit()
        self.inputline.setStyleSheet("font-size: 15px;")
        self.inputline.setPlaceholderText("Enter this first...")
        self.inputline.setAlignment(Qt.AlignCenter)

        self.label2 = QLabel("Enter FPS Below")
        self.label2.setStyleSheet("font-size: 15px; font-family: Arial;")
        self.label2.setAlignment(Qt.AlignCenter)

        self.inputline2 = QLineEdit()
        self.inputline2.setStyleSheet("font-size: 15px;")
        self.inputline2.setPlaceholderText("Then enter this...")
        self.inputline2.setAlignment(Qt.AlignCenter)

        self.button = QPushButton("Submit")
        self.button.setStyleSheet("font-size: 15px; font-family: Impact;")

        controls = QWidget(self)
        controls.setGeometry(0, 0, 600, 300)

        vbox = QVBoxLayout(controls)
        vbox.addWidget(self.label)
        vbox.addWidget(self.inputline)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.inputline2)
        vbox.addWidget(self.button)
        vbox.addStretch()

        self.pixmap = QPixmap(f"{self.Rim_Pic_File}")

        self.button.clicked.connect(self.Input)

    def Input(self):
        self.rpm = int(self.inputline.text())
        self.rps = self.rpm / 60
        self.dps = self.rps * 360
        self.Input2()

    def Input2(self):
        self.fps = int(self.inputline2.text())

        self.timer = QTimer(self)
        self.timer.start(int(1000 / self.fps))
        self.timer.timeout.connect(self.Update)

    def Update(self):
        self.angle %= 360
        self.angle += self.dps / self.fps
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = self.pixmap.scaled(500,500)

        x = self.width() // 2
        y = 3*self.height() // 5

        painter.translate(x, y)
        painter.rotate(self.angle)
        painter.translate(-pixmap.width()//2,-pixmap.height()//2)

        painter.drawPixmap(0,0,pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    rimspin = Rimspin()
    rimspin.show()
    sys.exit(app.exec_())