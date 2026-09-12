from PyQt5.QtGui import QIcon,QFontDatabase
import sys,requests
from PyQt5.QtWidgets import QApplication,QLabel,QVBoxLayout,QHBoxLayout,QPushButton,QWidget,QLineEdit
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(1150,150,350,600)

        import os
        from dotenv import load_dotenv
        load_dotenv()
        Icon_File = os.getenv("Icon_File")
        Font_File = os.getenv("Font_File")
        self.API_KEY = os.getenv("API_KEY")

        self.setWindowIcon(QIcon(f"{Icon_File}"))

        QFontDatabase.addApplicationFont(f"{Font_File}")
        self.initUI()

    def initUI(self):

        self.enterlabel = QLabel("Enter city name below:",self)
        self.enterlabel.setStyleSheet("font-size: 25px; font-weight: bold; font-family:italic;")
        self.cinput = QLineEdit(self)
        self.cinput.setPlaceholderText("Here...")
        self.button = QPushButton("Show Weather Data",self)
        self.button.setStyleSheet("font-size: 25px; font-family:Impact;")
        self.templabel = QLabel(self)
        self.emojilabel1 = QLabel(self)
        self.emojilabel1.setStyleSheet("font-size: 110px; font-family: Segoe UI emoji;")
        self.emojilabel2 = QLabel(self)
        self.emojilabel2.setStyleSheet("font-size: 110px; font-family: Segoe UI emoji;")
        self.desc = QLabel(self)
        self.desc.setStyleSheet("font-size: 40px; font-family:italic; font-weight: bold;")

        self.enterlabel.setAlignment(Qt.AlignCenter)
        self.cinput.setAlignment(Qt.AlignCenter)
        self.templabel.setAlignment(Qt.AlignCenter)
        self.desc.setAlignment(Qt.AlignCenter)
        self.emojilabel2.setAlignment(Qt.AlignCenter)
        self.emojilabel1.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(self.enterlabel)
        vbox.addWidget(self.cinput)
        vbox.addWidget(self.button)
        vbox.addWidget(self.templabel)
        self.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.emojilabel2)
        hbox.addWidget(self.emojilabel1)
        vbox.addLayout(hbox)
        
        vbox.addWidget(self.desc)

        self.button.clicked.connect(self.getweather)

    def getweather(self):

        city_name = self.cinput.text()
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.API_KEY}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            self.response = response.json()

            tempreture = self.response["main"]["temp"]-273
            self.templabel.setStyleSheet("font-size: 90px; font-family:Arial;")
            self.templabel.setText(f"{tempreture:.0f}°c")
            self.emoji()
            self.emoji2()
            self.Desc()
            self.cinput.clear()

        except requests.exceptions.HTTPError as e:

            errors = {400: "Error 400 - Bad Request",
                      401: "Error 401 - Unauthorized",
                      404: "Error 404 - Not Found",
                      429: "Error 429 - Too Many Requests"}

            self.templabel.setText(errors.get(e.response.status_code,"Error 5xx - Unexpected Error"))
            
            self.templabel.setStyleSheet("font-size: 20px; font-family:Arial;")
            self.emojilabel2.clear()
            self.emojilabel1.clear()
            self.desc.clear()
            self.cinput.clear()

        except requests.exceptions.RequestException:

            self.templabel.setText(f"Error 5xx - Unexpected Error")
            self.templabel.setStyleSheet("font-size: 20px; font-family:Arial;")
            self.emojilabel2.clear()
            self.emojilabel1.clear()
            self.desc.clear()
            self.cinput.clear()

    def emoji(self):
        response = self.response
        match response['weather'][0]['id']:

            case _ if 200 <= response["weather"][0]['id'] < 300:
                self.emojilabel1.setText("⛈️")

            case _ if 300 <= response["weather"][0]['id'] < 500:
                self.emojilabel1.setText("🌧️")

            case _ if 500 <= response["weather"][0]['id'] < 511:
                self.emojilabel1.setText("🌧️")

            case 511:
                self.emojilabel1.setText("❄️")

            case _ if 520 <= response["weather"][0]['id'] < 600:
                self.emojilabel1.setText("🌧️")

            case _ if 600 <= response["weather"][0]['id'] < 700:
                self.emojilabel1.setText("❄️")

            case _ if 700 <= response["weather"][0]['id'] < 800:
                self.emojilabel1.setText("🌪️")

            case 800:
                if self.response['weather'][0]['icon'][2] == 'd':
                    self.emojilabel1.setText("🌇")
                else:
                    self.emojilabel1.setText("🌃")
                    
            case _ if 800 < response["weather"][0]['id']:
                self.emojilabel1.setText("☁️")

    def emoji2(self):
        match self.response['weather'][0]['icon'][2]:

            case 'd':
                self.emojilabel2.setText("☀️")

            case 'n':
                self.emojilabel2.setText("🌙")

    def Desc(self):
        self.desc.setText(self.response['weather'][0]['description'])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weatherApp = WeatherApp()
    weatherApp.show()
    sys.exit(app.exec_())
