from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from truss import Truss  

class plotCalc(QWidget):
    def __init__(self,truss: Truss):
        super().__init__()
        self.truss = truss
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Create a matplotlib figure
        fig = Figure()
        self.canvas = FigureCanvas(fig)
        layout.addWidget(self.canvas)

        # Create an axis for the figure
        self.ax = fig.add_subplot(111, projection='3d')

        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title('Treliça')

        self.canvas.draw()
