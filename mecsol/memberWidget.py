from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from truss import Truss

class MemberWidget(QDialog):
    def __init__(self, truss: Truss, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Member Widget")
        self.truss = truss
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Member id
        id_label = QLabel("ID Conexões")
        self.id_input = QLineEdit()
        layout.addWidget(id_label)
        layout.addWidget(self.id_input)

        # Node A
        NodeA_label = QLabel("Ponto A")
        self.NodeA_input = QLineEdit()
        layout.addWidget(NodeA_label)
        layout.addWidget(self.NodeA_input)

        # Node B
        NodeB_label = QLabel("Ponto B")
        self.NodeB_input = QLineEdit()
        layout.addWidget(NodeB_label)
        layout.addWidget(self.NodeB_input)

        # Salvar
        button = QPushButton("Salvar")
        button.clicked.connect(self.save_members)
        layout.addWidget(button)

    def save_members(self):
        id = self.id_input.text() #nome da conexão 

        #ID dos pontos que vão possuir a conexão 
        nodeA = self.NodeA_input.text()
        nodeB = self.NodeB_input.text()

        #Procura a posição que as caracteristicas dos elementos vão estar 
        try:
            listA = self.truss.getID()

            self.dA = listA.index(nodeA)
            self.dB = listA.index(nodeB)

            self.truss.setMembersID(id)
            self.truss.setMembers(nodeA, nodeB)

            print(self.dA)
            print(self.dB)

            self.truss.setMembersX(self.dA,self.dB)
            self.truss.setMembersY(self.dA,self.dB)
            self.truss.setMembersZ(self.dA,self.dB)
            self.truss.setMembers(self.dA,self.dB)
            self.truss.setFlagM(True) #True means a member was put and must be ploted
        except:
            QMessageBox.about(self,"Erro","Node invalido inserido")

        self.accept()

