import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create the QWebEngineView
        self.view = QWebEngineView(self)
        self.view.setUrl(QUrl("https://www.google.com"))
        
        # Create the back button
        self.back_button = QPushButton("<", self)
        self.back_button.clicked.connect(self.view.back)
        
        # Create the forward button
        self.forward_button = QPushButton(">", self)
        self.forward_button.clicked.connect(self.view.forward)
        
        # Create the refresh button
        self.refresh_button = QPushButton("Refresh", self)
        self.refresh_button.clicked.connect(self.view.reload)
        
        # Create the address bar
        self.address_bar = QTextEdit(self)
        self.address_bar.setText(self.view.url().toString())
        self.address_bar.returnPressed.connect(self.navigate_to_url)
        
        # Create the layout
        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.forward_button)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.address_bar)
        layout.addWidget(self.view)
        
        # Set the layout
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
    def navigate_to_url(self):
        url = self.address_bar.text()
        self.view.setUrl(QUrl(url))

app = QApplication(sys.argv)
browser = Browser()
browser.show()
app.exec_()
