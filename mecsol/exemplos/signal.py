import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True 

        self.setWindowTitle("My app")

        button = QPushButton("Press me")
        button.setCheckable(True) #ativa o botão 
        #event 
        button.clicked.connect(self.the_button_was_toggled) 
        button.setChecked(self.button_is_checked)

        self.setCentralWidget(button)

    
    
    def the_button_was_toggled(self,checked):
        self.button_is_checked = checked 
        
        print("Checked:",checked)
        

    


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
