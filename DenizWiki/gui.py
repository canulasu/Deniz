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
    mobile = False
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.wikipedia.org/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        backbutton = QAction('Back', self)
        backbutton.triggered.connect(self.browser.back)
        navbar.addAction(backbutton)

        forawrdbutton = QAction('Forward', self)
        forawrdbutton.triggered.connect(self.browser.forward)
        navbar.addAction(forawrdbutton)

        rebutton = QAction('Reload', self)
        rebutton.triggered.connect(self.browser.reload)
        navbar.addAction(rebutton)

        homebtn = QAction('Home', self)
        homebtn.triggered.connect(self.navigate_home)
        navbar.addAction(homebtn)

        ranbtn = QAction('Random Page', self)
        ranbtn.triggered.connect(self.navigate_random)
        navbar.addAction(ranbtn)

        mobilebtn = QAction('Mobile', self)
        mobilebtn.triggered.connect(self.navigate_mobile)
        navbar.addAction(mobilebtn)

        self.browser.urlChanged.connect(self.security)

    def security(self):
        if 'https://' not in self.browser.url().toString():
            self.browser.setUrl(QUrl('https://en.wikipedia.org/wiki/Malware'))
        if self.browser.url().toString() == 'https://www.stormfront.org':
            self.browser.setUrl(QUrl('https://en.wikipedia.org/wiki/Malware'))


    def navigate_custom(self):
        url = self.urlbar.text()
        if 'https://' not in url:
            searchengine = 'https://www.google.com/search?q=' + url
            print(searchengine)
            self.browser.setUrl(QUrl('https://en.wikipedia.org/wiki/Malware'))
        if url == 'https://www.stormfront.org':
            self.browser.setUrl(QUrl('https://en.wikipedia.org/wiki/Malware'))
        else:
            self.browser.setUrl(QUrl(url))

    def navigate_mobile(self):
        if self.mobile == False:
            self.setFixedSize(360, 640)
            self.mobile = True
        else:
            self.setFixedSize(1460, 820)
            self.mobile = False

    def navigate_random(self):
        self.browser.setUrl(QUrl('https://en.wikipedia.org/wiki/Special:Random'))


    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.wikipedia.org/'))



app = QApplication(sys.argv)
QApplication.setApplicationName('Jakaranda Search')
window = MainWindow()
app.exec_()