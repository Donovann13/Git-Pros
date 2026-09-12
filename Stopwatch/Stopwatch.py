import sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QLabel
from PyQt5.QtCore import Qt,QTimer,QTime
from PyQt5.QtGui import QIcon

class stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("00:00:00.00",self)
        self.time = QTime(0,0,0,0)
        self.timer = QTimer()
        self.startbutton = QPushButton("Start",self)
        self.stopbutton = QPushButton("Stop",self)
        self.resetbutton = QPushButton("Reset",self)

        import os
        from dotenv import load_dotenv
        load_dotenv()
        Icon_File = os.getenv("Icon_File")
        self.setWindowIcon(QIcon(f"{Icon_File}"))
        self.setWindowTitle("Stopwatch")
        self.setGeometry(800,300,650,350)
        self.initUI()

    def initUI(self):

        self.time_label.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.startbutton)
        hbox.addWidget(self.stopbutton)
        hbox.addWidget(self.resetbutton)
        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QPushButton,QLabel{
                font-size: 50px;
                font-family: Impact;       
            }
            QLabel{
                background-color:#98E3D5;    
                border-radius: 10px;
            }
        """)

        self.startbutton.clicked.connect(self.Start)
        self.stopbutton.clicked.connect(self.Stop)
        self.resetbutton.clicked.connect(self.Reset)

        self.timer.timeout.connect(self.Update)

    def Start(self):
        self.timer.start(10)

    def Stop(self):
        self.timer.stop()

    def Reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.Display(self.time))

    def Update(self):
            self.time = self.time.addMSecs(10)
            self.time_label.setText(self.Display(self.time))

    def Display(self,time):
        return f"{time.hour():02}:{time.minute():02}:{time.second():02}.{(time.msec())//10:02}"
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Stopwatch = stopwatch()
    Stopwatch.show()
    sys.exit(app.exec_())