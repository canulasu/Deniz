import subprocess

filename = 'PyQt5'

try:
    subprocess.check_call(["pip", "install", f"{filename}"])
except:
    try:
        subprocess.check_call(["pip3", "install", f"{filename}"])
    except:
        print('ERROR: Could not install dependencies')

filename = 'PyQtWebEngine'

try:
    subprocess.check_call(["pip", "install", f"{filename}"])
except:
    try:
        subprocess.check_call(["pip3", "install", f"{filename}"])
    except:
        print('ERROR: Could not install dependencies')

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://login.arduino.cc/login?state=hKFo2SBHSnBVelVtdHZqbTR1NkNmbDhiTE5TQThGcHhKLW5Xa6FupWxvZ2luo3RpZNkgTDhjN2JVQkxTNkV0WlMtTFBISjI1LWhwelNaWGNRWFajY2lk2SBVWEh1bTludjdYa3BFVE1wbTZQaTRUZzJGcG9QcG1oVw&client=UXHum9nv7XkpETMpm6Pi4Tg2FpoPpmhW&protocol=oauth2&scope=openid+profile+email&redirect_uri=https%3A%2F%2Fapp.arduino.cc%2Fsketches%2Fredirect&logout_uri=https%3A%2F%2Fapp.arduino.cc%2Fsketches&audience=https%3A%2F%2Fapi.arduino.cc&response_type=code&response_mode=query&nonce=VzlpaE42b35CaWIta3R%2BQmNkNFAxQWF6WE4waFhKdmpXTHJXMmxTTXBBMw%3D%3D&code_challenge=UwJ8rg9JkHb_qaJoS28Y7pdoa9pRz2CJ8Nncsafq1ys&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtc3BhLWpzIiwidmVyc2lvbiI6IjIuMS4zIn0%3D#/sso/login'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


    
app = QApplication(sys.argv)
QApplication.setApplicationName('Client')
window = MainWindow()
app.exec_()