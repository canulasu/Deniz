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
        self.browser.setUrl(QUrl('https://start.me/p/aNdJ6m/pagina-de-inicio'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        self.setWindowTitle('Van Kedisi Browser')

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

        tabbtn = QAction('New Tab', self)
        tabbtn.triggered.connect(self.new_tab)
        navbar.addAction(tabbtn)

        self.urlbar = QLineEdit(self)
        self.urlbar.returnPressed.connect(self.navigate_custom)
        navbar.addWidget(self.urlbar)

        self.browser.urlChanged.connect(self.security)

    def security(self):
        if 'https://' not in self.browser.url().toString():
            self.browser.setUrl(QUrl('https://sites.google.com/view/jdhow5h7q0hf0unuhtq07438fu8hf/home'))
        if self.browser.url().toString() == 'https://www.stormfront.org':
            self.browser.setUrl(QUrl('https://sites.google.com/view/jdhow5h7q0hf0unuhtq07438fu8hf/home'))

    def new_tab(self):
        subprocess.Popen([sys.executable, __file__])


    def navigate_custom(self):
        url = self.urlbar.text()
        if 'https://' not in url:
            searchengine = 'https://www.google.com/search?q=' + url
            print(searchengine)
            self.browser.setUrl(QUrl('https://sites.google.com/view/jdhow5h7q0hf0unuhtq07438fu8hf/home'))
        if url == 'https://www.stormfront.org':
            self.browser.setUrl(QUrl('https://sites.google.com/view/jdhow5h7q0hf0unuhtq07438fu8hf/home'))
        else:
            self.browser.setUrl(QUrl(url))



    def navigate_home(self):
        self.browser.setUrl(QUrl('https://start.me/p/aNdJ6m/pagina-de-inicio'))



app = QApplication(sys.argv)
QApplication.setApplicationName('Jakaranda Search')
window = MainWindow()
app.exec_()
