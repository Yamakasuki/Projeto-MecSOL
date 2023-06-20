import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QGridLayout, QSpacerItem, QSizePolicy, QAction
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QBrush, QColor
from PyQt5.QtCore import Qt, QSize, QRect


class CircleIconWidget(QWidget):
    def __init__(self, icon_path, size, parent=None):
        super().__init__(parent)
        self.icon_path = icon_path
        self.size = size

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw circle
        diameter = min(self.size.width(), self.size.height())
        radius = diameter / 2
        center = self.rect().center()
        circle_rect = QRect(center.x() - radius, center.y() - radius, diameter, diameter)

        # Fill circle with icon image
        icon = QIcon(self.icon_path).pixmap(diameter, diameter)
        painter.setBrush(QBrush(icon))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(circle_rect)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Window properties
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 900, 900)

        # Create central widget and main layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Left side (Sidebar) with five buttons
        self.left_side = QWidget(self)
        self.left_side.setObjectName("left_side")
        self.left_layout = QVBoxLayout()
        self.left_side.setLayout(self.left_layout)

        for i in range(4):
            button = QPushButton(f"Button {i+1}", self)
            self.left_layout.addWidget(button)  # Add buttons to the layout

        self.spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.left_layout.addItem(self.spacer)  # Add vertical spacer

        button5 = QPushButton("Button 5", self)
        self.left_layout.addWidget(button5)  # Add button 5

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

        # Set sizes for left and right sides
        main_layout.addWidget(self.left_side, 1)  # Smaller size
        main_layout.addWidget(right_side, 3)  # Larger size

        # Set background colors for left and right sides
        self.left_side.setStyleSheet("background-color: lightgray;")
        right_side.setStyleSheet("background-color: white;")

        # Toggle action for showing/hiding the sidebar
        toggle_action = QAction(self)
        toggle_action.setIcon(QIcon("icons/menu_icon.png"))
        toggle_action.triggered.connect(self.toggle_sidebar)

        # Create custom circle icon widget
        icon_widget = CircleIconWidget("icons/menu_icon.png", QSize(24, 24), self)
        icon_widget.setStyleSheet("background-color: transparent;")

        # Create toolbar and add toggle action with the circle icon widget
        toolbar = self.addToolBar("Toolbar")
        toolbar.addWidget(icon_widget)
        toolbar.addAction(toggle_action)

    def toggle_sidebar(self):
        if self.left_side.isHidden():
            self.left_side.show()
            self.spacer.changeSize(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        else:
            self.left_side.hide()
            self.spacer.changeSize(0, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        self.left_side.layout().invalidate()
        self.left_side.layout().activate()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
