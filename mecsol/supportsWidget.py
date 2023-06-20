from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon
from truss import Truss

class SupportsWidget(QDialog):
    def __init__(self, truss: Truss, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Support Widget")
        self.truss = truss
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Point ID
        point_id_label = QLabel("Ponto ID:")
        self.point_id_input = QLineEdit()
        layout.addWidget(point_id_label)
        layout.addWidget(self.point_id_input)

        # Buttons Layout
        buttons_layout = QGridLayout()
        layout.addLayout(buttons_layout)

        # Pino
        button1 = QPushButton()
        button1.setIcon(QIcon("icons/pino.png"))  # Set the icon path
        button1.setFixedSize(40, 40)  # Set a fixed size for the button
        button1.clicked.connect(self.button1_clicked)  # Connect the clicked signal
        buttons_layout.addWidget(button1, 0, 0)

        # Rolamento 
        button2 = QPushButton()
        button2.setIcon(QIcon("icons/rolamento.png"))  # Set the icon path
        button2.setFixedSize(40, 40)  # Set a fixed size for the button
        button2.clicked.connect(self.button2_clicked)  # Connect the clicked signal
        buttons_layout.addWidget(button2, 0, 1)

        # Engaste
        button3 = QPushButton()
        button3.setIcon(QIcon("icons/engaste.png"))  # Set the icon path
        button3.setFixedSize(40, 40)  # Set a fixed size for the button
        button3.clicked.connect(self.button3_clicked)  # Connect the clicked signal
        buttons_layout.addWidget(button3, 1, 0)


    def button1_clicked(self):
        self.tipo = self.point_id_input.text()
        self.truss.setSupports("pino",self.tipo)
        self.flag_s = True


    def button2_clicked(self):
        self.tipo = self.point_id_input.text()
        self.truss.setSupports("rolete",self.tipo)
        self.flag_s = True


    def button3_clicked(self):
        self.tipo = self.point_id_input.text()
        self.truss.setSupports("engaste",self.tipo)
        self.flag_s = True



