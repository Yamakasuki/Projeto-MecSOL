import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtUiTools import QUiLoader

class Sidebar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Load the UI file
        loader = QUiLoader()
        ui_file = QFile("sidebar.ui")
        ui_file.open(QFile.ReadOnly)
        self.sidebar_widget = loader.load(ui_file)
        ui_file.close()

        # Set the layout for the sidebar widget
        layout = QVBoxLayout()
        layout.addWidget(self.sidebar_widget)
        self.setLayout(layout)

# Create the main application window
app = QApplication(sys.argv)
window = QWidget()

# Create the sidebar widget
sidebar = Sidebar()

# Create a layout for the main window
layout = QVBoxLayout()

# Add the sidebar to the layout
layout.addWidget(sidebar)

# Set the layout for the main window
window.setLayout(layout)

# Show the main window
window.show()

# Start the event loop
sys.exit(app.exec_())

