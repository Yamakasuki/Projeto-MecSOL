from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QMainWindow 
import sys

#Sunclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")
        button = QPushButton("Press me")
        #Set the size of the widget
        self.setFixedSize(QSize(1500,900))
        #Set the central widget of the window 
        self.setCentralWidget(button)





app = QApplication(sys.argv)

window = MainWindow()
window.show()


#começa o loop 
app.exec()
