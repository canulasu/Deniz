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
        self.browser.setUrl(QUrl('https://studio.youtube.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


    
app = QApplication(sys.argv)
QApplication.setApplicationName('Client')
window = MainWindow()
app.exec_()