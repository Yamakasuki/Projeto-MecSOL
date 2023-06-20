from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from truss import Truss  
import math

from truss1 import Result, init_truss, plot_diagram

class plotCalc(QWidget):
    def __init__(self,truss: Truss):
        super().__init__()
        self.truss = truss
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        # initialise Truss object
        my_truss = init_truss('My first truss')

        # set the (x, y) locations of the joints - places where bars, loads or supports can be placed
        my_truss.add_joints([(0, 0), (290, -90), (815, 127.5), (290, 345), (0, 255), (220.836, 127.5)])

        # join some joints together with bars - joints are named 
        # 'A', 'B', 'C', ... automatically in the order they were listed
        my_truss.add_bars(['AB', 'BC', 'CD', 'DE', 'EF', 'AF', 'DF', 'BF'])

        # add a load at the named joint
        my_truss.add_loads([('W', 'C', 0, -0.675)])

        # add two supports at the named joints
        my_truss.add_supports([('A', 'encastre'), ('E', 'pin', -math.pi / 2)])

        # Create a matplotlib figure
        fig = Figure()
        self.canvas = FigureCanvas(fig)
        layout.addWidget(self.canvas)

        # Create an axis for the figure
        my_truss.solve_and_plot()

        self.canvas.draw()
