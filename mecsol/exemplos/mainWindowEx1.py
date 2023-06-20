import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Window properties
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)

        # Create central widget and main layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Left side (Sidebar) with five buttons
        left_side = QWidget(self)
        left_side.setObjectName("left_side")
        left_layout = QVBoxLayout()
        left_side.setLayout(left_layout)

        for i in range(5):
            button = QPushButton(f"Button {i+1}", self)
            left_layout.addWidget(button)

        # Right side divided into two widgets
        right_side = QWidget(self)
        right_side.setObjectName("right_side")
        right_layout = QVBoxLayout()
        right_side.setLayout(right_layout)

        # Placeholder for 3D graph
        graph_widget = QLabel("Graph Widget", self)
        graph_widget.setObjectName("graph_widget")
        graph_widget.setStyleSheet("background-color: lightblue;")

        # Placeholder for table
        table_widget = QLabel("Table Widget", self)
        table_widget.setObjectName("table_widget")
        table_widget.setStyleSheet("background-color: lightgreen;")

        # Add widgets to the right layout
        right_layout.addWidget(graph_widget)
        right_layout.addWidget(table_widget)

        # Add left and right sides to the main layout
        main_layout.addWidget(left_side)
        main_layout.addWidget(right_side)

        # Set background colors for left and right sides
        left_side.setStyleSheet("background-color: lightgray;")
        right_side.setStyleSheet("background-color: white;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
