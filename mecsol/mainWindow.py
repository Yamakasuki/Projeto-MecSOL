import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QLabel, QVBoxLayout, QAction
from PyQt5.QtGui import QIcon
from leftside import LeftSideWidget
from graphWidget import GraphWidget
from plotCalc import plotCalc
from truss import Truss
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.truss = Truss()
        self.flag = self.truss.getFlagC()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 900, 900)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        #left sideWidget 
        self.left_side = LeftSideWidget(self.truss)
        main_layout.addWidget(self.left_side, 1)  # Smaller size
        
        #Rigth side widget 
        right_side = QWidget(self)
        right_layout = QVBoxLayout(right_side)
        right_side.setLayout(right_layout)

        # Create a QTimer to periodically update the plot
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)  # Update every 1 second

        self.graph_widget = GraphWidget(self.truss)
        self.calcWidget = plotCalc(self.truss)
        if (self.flag== False):
            right_layout.addWidget(self.graph_widget)
        else:
            right_layout.addWidget(self.calcWidget)
         #cria um modulo q nem os outros chama de table_widget e monta a tela naquele modulo
        
        #AQUI  
   
        table_widget = QWidget()
        table_widget.setObjectName("table_widget")
        table_widget.setStyleSheet("background-color: lightgreen;")
        table_layout = QVBoxLayout(table_widget)

        right_layout.addWidget(table_widget)

        main_layout.addWidget(right_side, 3)  # Larger size

        right_side.setStyleSheet("background-color: white;")

        toggle_action = QAction(self)
        toggle_action.setIcon(QIcon("icons/menu_icon.png"))
        toggle_action.triggered.connect(self.toggle_sidebar)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(toggle_action)
        
    def toggle_sidebar(self):
        if self.left_side.isHidden():
            self.left_side.show()
        else:
            self.left_side.hide()
def update(self):
        self.flag = self.getflagC()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
