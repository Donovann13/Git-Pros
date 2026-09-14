import os,pygame,sys
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QRadioButton,QButtonGroup,QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QIcon,QFont
from dotenv import load_dotenv

class Music_Player(QWidget):
    def __init__(self):
        super().__init__()

        load_dotenv()
        self.folder_path = os.getenv("folder_path")
        icon_file = os.getenv("icon_file")

        self.filesl = os.listdir(self.folder_path)

        self.setWindowTitle("Music Player")
        self.setWindowIcon(QIcon(icon_file))
        self.setGeometry(1200,80,400,300)

        self.box = QLineEdit(self)
        self.box.setPlaceholderText("Enter # here to play...")
        self.box.setFont(QFont("italic",10))

        self.button = QPushButton("Submit",self)
        self.button.setFont(QFont("impact",13))

        self.error = QLabel("",self)
        self.error.setFont(QFont("impact",15))
        self.error.hide()

        self.vbox = QVBoxLayout(self)
        
        self.vbox.addWidget(self.box)
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.error)

        for index,filename in enumerate(self.filesl):
            hbox = QHBoxLayout()
            label = QLabel(f"{index+1}. {filename}",self)
            hbox.addWidget(label)
            self.vbox.addLayout(hbox)

        hbox2 = QHBoxLayout()
        
        radio_group = QButtonGroup(self)
        self.radio1 = QRadioButton("Pause")
        self.radio2 = QRadioButton("Resume")
        self.radio3 = QRadioButton("Stop")
        radio_group.addButton(self.radio1)
        radio_group.addButton(self.radio2)
        radio_group.addButton(self.radio3)
        hbox2.addWidget(self.radio1)
        hbox2.addWidget(self.radio2)
        hbox2.addWidget(self.radio3)

        self.vbox.insertLayout(0,hbox2)

        self.button.clicked.connect(self.Play)

    def Play(self):

        choice = self.box.text()
        if not choice.isdigit() or not (0 < int(choice) <= len(self.filesl)):
            self.error.setText("----Invalid Input!----")
            self.error.show()
        else:
            self.error.clear()
            filename = os.listdir(self.folder_path)[int(choice)-1]
            sound_file = os.path.join(self.folder_path,filename)
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
        self.radio1.toggled.connect(self.Pause)
        self.radio2.toggled.connect(self.Resume)
        self.radio3.toggled.connect(self.Stop)

        self.box.clear()

    def Pause(self):
        pygame.mixer.music.pause()
    def Resume(self):
        pygame.mixer.music.unpause()
    def Stop(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    music_player = Music_Player()
    music_player.show()
    sys.exit(app.exec_())