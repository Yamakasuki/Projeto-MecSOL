from PyQt5.QtWidgets import QSizePolicy, QSpacerItem, QHBoxLayout, QWidget, QLabel, QVBoxLayout, QAction, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize
from pointWidget import PointWidget 
from memberWidget import MemberWidget
from forceWidget import ForceWidget 
from supportsWidget import SupportsWidget
import solver as sv
from truss import Truss

class LeftSideWidget(QWidget):
    def __init__(self,trss: Truss, parent=None):
        super().__init__(parent)
        #objeto com as caracteristicas da treliça 
        self.truss = trss
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Header
        header_label = QLabel("Truss calc", self)
        header_label.setObjectName("header_label")
        header_label.setStyleSheet("font-family: Open Sans; font-size: 30px;")
        layout.addWidget(header_label)

        # Image label
        image_label = QLabel(self)
        image_label.setObjectName("image_label")
        pixmap = QPixmap("icons/bridge.png").scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)

        # Spacer
        layout.addSpacing(20)

        # Button 1: Pontos
        button_pontos = QPushButton("Pontos", self)
        button_pontos.setObjectName("button_pontos")
        button_pontos.setStyleSheet("QPushButton { padding: 10px; font-family: Open Sans; font-size: 20px; background-color: #84e4a8; border-radius: 10px; }")
        button_pontos.setCheckable(True)
        button_pontos.clicked.connect(self.button_pontos_clicked)
        layout.addWidget(button_pontos)

        # Button 2: Conexões
        button_conexoes = QPushButton("Conexões", self)
        button_conexoes.setObjectName("button_conexoes")
        button_conexoes.setStyleSheet("QPushButton { padding: 10px; font-family: Open Sans; font-size: 20px; background-color: #84e4a8; border-radius: 10px; }")
        button_conexoes.setCheckable(True)
        button_conexoes.clicked.connect(self.button_conexoes_clicked)
        layout.addWidget(button_conexoes)

        # Button 3: Forças
        button_forcas = QPushButton("Forças", self)
        button_forcas.setObjectName("button_forcas")
        button_forcas.setStyleSheet("QPushButton { padding: 10px; font-family: Open Sans; font-size: 20px; background-color: #84e4a8; border-radius: 10px; }")
        button_forcas.setCheckable(True)
        button_forcas.clicked.connect(self.button_forcas_clicked)
        layout.addWidget(button_forcas)

        # Button 4: Suportes
        button_suportes = QPushButton("Suportes", self)
        button_suportes.setObjectName("button_suportes")
        button_suportes.setStyleSheet("QPushButton { padding: 10px; font-family: Open Sans; font-size: 20px; background-color: #84e4a8; border-radius: 10px; }")
        button_suportes.setCheckable(True)
        button_suportes.clicked.connect(self.button_suportes_clicked)
        layout.addWidget(button_suportes)

        # Spacer
        layout.addStretch()

        # Button 5: Calcular
        button_calcular = QPushButton("Calcular", self)
        button_calcular.setObjectName("button_calcular")
        button_calcular.setStyleSheet("QPushButton { padding: 10px; font-family: Open Sans; font-size: 20px; background-color: #84e4a8; border-radius: 10px; }")
        button_calcular.setCheckable(True)
        button_calcular.clicked.connect(self.button_calcular_clicked)
        layout.addWidget(button_calcular)

        self.setStyleSheet(
            "LeftSideWidget { background-color: #3e4b51; }"
            "#header_label { background-color: #bcbefa; }"
            "#image_label { background-color: #bcbefa; }"
        )

    def button_pontos_clicked(self):
        print("Button Pontos clicked")
        self.point_dialog = PointWidget(self.truss, self)
        self.point_dialog.exec_()


    def button_conexoes_clicked(self):
        print("Button Conexões clicked")
        self.conexoes_dialog = MemberWidget(self.truss,self)
        self.conexoes_dialog.exec_()
   
    def button_forcas_clicked(self):
        print("Button Forças clicked")
        self.forcas_dialog = ForceWidget(self.truss,self)
        self.forcas_dialog.exec_()

    def button_suportes_clicked(self):
        print("Button Suportes clicked")
        self.suportes_dialog= SupportsWidget(self.truss,self)
        self.suportes_dialog.exec_()


    def button_calcular_clicked(self):
        self.truss.get
        


