import sys
from PyQt5.QtCore import Qt,QTimer,QTime
from PyQt5.QtWidgets import QApplication,QLabel,QVBoxLayout,QWidget
from PyQt5.QtGui import QFontDatabase,QFont,QIcon

class Clock(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Digital Clock')

        import os
        from dotenv import load_dotenv
        load_dotenv()
        Icon_File = os.getenv("Icon_File")
        self.Font_File = os.getenv("Font_File")
         
        self.setWindowIcon(QIcon(f"{Icon_File}"))
        self.setGeometry(750, 300, 850, 250)
        self.time_label = QLabel(self)
        self.timer = QTimer()
        self.setStyleSheet("background-color: black;")
        self.initUI()

    def initUI(self):
        font_id = QFontDatabase.addApplicationFont(f"{self.Font_File}")
        my_font = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.time_label.setFont(QFont(my_font,150))
        self.time_label.setStyleSheet("color: green;")
        self.time_label.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.timer.timeout.connect(self.updater)
        self.timer.start(1000)

    def updater(self):
        self.current = QTime.currentTime().toString("hh:mm:ss A")
        self.time_label.setText(self.current)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Clock()
    clock.show()
    sys.exit(app.exec_())