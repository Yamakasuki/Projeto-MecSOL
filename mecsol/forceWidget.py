from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from truss import Truss

class ForceWidget(QDialog):
    def __init__(self, truss: Truss, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Force Widget")
        self.truss = truss
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout(self)
        
        # Node id
        id_label = QLabel("Ponto ID")
        self.id_input = QLineEdit()
        layout.addWidget(id_label)
        layout.addWidget(self.id_input)

        # Magnitude X
        magX_label = QLabel("Magnitude X")
        self.magX_input = QLineEdit()
        layout.addWidget(magX_label)
        layout.addWidget(self.magX_input)

        # Magnitude Y
        magY_label = QLabel("Magnitude Y")
        self.magY_input = QLineEdit()
        layout.addWidget(magY_label)
        layout.addWidget(self.magY_input)

        
        # Magnitude Z
        magZ_label = QLabel("Magnitude Z")
        self.magZ_input = QLineEdit()
        layout.addWidget(magZ_label)
        layout.addWidget(self.magZ_input)

        # Salvar
        button = QPushButton("Salvar")
        button.clicked.connect(self.save_members)
        layout.addWidget(button)

    def save_members(self):
        id = self.id_input.text()
        x = float(self.magX_input.text())
        y = float(self.magY_input.text())
        z = float(self.magZ_input.text())

        self.truss.setForcesID(id) #É onde a força está localizada
        self.truss.setForcesx(x)
        self.truss.setForcesy(y)
        self.truss.setForcesz(z)

        self.truss.setForcesFlag(True)

        self.accept()
