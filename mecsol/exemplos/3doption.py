import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Graph Surface")
        self.setup_ui()
        self.points = []  # List to store the plotted points

    def setup_ui(self):
        # Create main widget and layout
        main_widget = QWidget(self)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Create sidebar widget and layout
        sidebar_widget = QWidget(self)
        sidebar_layout = QFormLayout()
        sidebar_widget.setLayout(sidebar_layout)
        main_layout.addWidget(sidebar_widget)

        # Create input fields for x, y, and z values
        self.x_input = QLineEdit()
        self.y_input = QLineEdit()
        self.z_input = QLineEdit()
        sidebar_layout.addRow(QLabel("X:"), self.x_input)
        sidebar_layout.addRow(QLabel("Y:"), self.y_input)
        sidebar_layout.addRow(QLabel("Z:"), self.z_input)

        # Create input field for point name
        self.point_name_input = QLineEdit()
        sidebar_layout.addRow(QLabel("Point Name:"), self.point_name_input)

        # Create plot button
        plot_button = QPushButton("Plot")
        plot_button.clicked.connect(self.plot_graph)
        sidebar_layout.addRow(plot_button)

        # Create matplotlib widget for displaying the graph
        self.graph_widget = plt.figure()
        main_layout.addWidget(self.graph_widget.canvas)

    def plot_graph(self):
        # Retrieve x, y, and z values from input fields
        x = float(self.x_input.text())
        y = float(self.y_input.text())
        z = float(self.z_input.text())

        # Store the plotted point in the list
        self.points.append((x, y, z))

        # Clear previous plot
        self.graph_widget.clear()

        # Set the wireframe color to none
        plt.rcParams['plot3d.surfacecolors'] = 'none'

        # Create 3D axis
        ax = self.graph_widget.add_subplot(111, projection='3d')

        # Plot the points
        for point in self.points:
            x, y, z = point
            ax.scatter(x, y, z, color='red', s=50)
            ax.text(x, y, z, f"({x}, {y}, {z})", color='black')

        # Set labels and title
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Plotted Points')

        # Update the plot
        self.graph_widget.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
