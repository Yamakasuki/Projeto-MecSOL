from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from truss import Truss

class PointWidget(QDialog):
    def __init__(self, truss: Truss, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Point Widget")
        self.truss = truss
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
          
        # Posição X
        x_label = QLabel("Posição X:")
        self.x_input = QLineEdit()
        layout.addWidget(x_label)
        layout.addWidget(self.x_input)

        # Posição Y
        y_label = QLabel("Posição Y:")
        self.y_input = QLineEdit()
        layout.addWidget(y_label)
        layout.addWidget(self.y_input)

        # Posição Z
        z_label = QLabel("Posição Z:")
        self.z_input = QLineEdit()
        layout.addWidget(z_label)
        layout.addWidget(self.z_input)

        # ID do ponto
        name_label = QLabel("ID do ponto:")
        self.name_input = QLineEdit()
        layout.addWidget(name_label)
        layout.addWidget(self.name_input)

        #Salvar
        button = QPushButton("Salvar")
        button.clicked.connect(self.save_point)
        layout.addWidget(button)

    def save_point(self):
        try:
            self.truss.setFlag(True)
            x = float(self.x_input.text())
            y = float(self.y_input.text())
            z = float(self.z_input.text())
            point_id = self.name_input.text()

            self.truss.setXpositions(x)
            self.truss.setYpositions(y)
            self.truss.setZpositions(z)
            self.truss.setID(point_id)
        except:
            QMessageBox.about(self,"Erro","Valor de coordenada inserido inválido")
        self.accept()

