import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QFont

class CartesianPlane(QWidget):
    def __init__(self):
        super(CartesianPlane, self).__init__()
        self.setWindowTitle("Cartesian Plane")
        self.setGeometry(100, 100, 600, 600)
        self.points = [(2, 4), (5, -3), (-3, 6)]  # Example points

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw Cartesian plane
        width = self.width()
        height = self.height()
        painter.drawLine(0, height // 2, width, height // 2)  # X-axis
        painter.drawLine(width // 2, 0, width // 2, height)  # Y-axis

        # Plot points and display coordinates
        painter.setPen(QPen(QColor(255, 0, 0), 5))  # Red color, 5-pixel width
        font = QFont("Arial", 10)
        painter.setFont(font)
        for point in self.points:
            x = width // 2 + point[0] * 20  # Scale factor of 20
            y = height // 2 - point[1] * 20  # Scale factor of 20
            painter.drawPoint(x, y)
            painter.drawText(x + 5, y - 5, f"({point[0]}, {point[1]})")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CartesianPlane()
    widget.show()
    sys.exit(app.exec_())
