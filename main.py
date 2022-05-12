from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    
    def go_home(self):
        self.browser.setUrl(QUrl('https://webradiobg.com'))
        
    def go_url (self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
        
    def update_url(self, url):
        self.url_bar.setText(url.toString())
        
            
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        #barra de navegação
        navbar = QToolBar()
        self.addToolBar(navbar)
        
        #botão de voltar a página
        voltar_btn = QAction('<-', self)
        voltar_btn.triggered.connect(self.browser.back)
        navbar.addAction(voltar_btn) 
        
        #botão de avançar a página
        seguir_btn = QAction('->', self)
        seguir_btn.triggered.connect(self.browser.forward)
        navbar.addAction(seguir_btn)
        
        #botão de refresh (atualizar)
        refresh_btn = QAction('Recarregar', self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)
        
        #botão home
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.go_home)
        navbar.addAction(home_btn)
        
        #barra de endereço
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.go_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)
        
        

 
    
app = QApplication(sys.argv)
QApplication.setApplicationName('new_browser')
windows = MainWindow()

app.exec()     


        
 
 

