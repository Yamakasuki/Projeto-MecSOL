import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QFont

class CartesianPlane(QWidget):
    def __init__(self):
        super(CartesianPlane, self).__init__()
        self.setWindowTitle("Cartesian Plane")
        self.setGeometry(100, 100, 700, 700)
        self.points = [(2, 4), (5, -3), (-3, 6)]  # Example points

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw Cartesian plane
        width = self.width()
        height = self.height()
        half_width = width // 2
        half_height = height // 2
        axis_color = QColor(0, 0, 0)
        grid_color = QColor(200, 200, 200)
        text_color = QColor(0, 0, 0)
        axis_pen = QPen(axis_color)
        grid_pen = QPen(grid_color)
        text_font = QFont("Arial", 10)

        painter.setPen(axis_pen)
        painter.drawLine(0, half_height, width, half_height)  # X-axis
        painter.drawLine(half_width, 0, half_width, height)  # Y-axis

        painter.setPen(grid_pen)
        painter.setFont(text_font)

        # Draw tick marks and labels on X-axis
        x_ticks = range(-20, 20)  # Tick marks range from -10 to 10
        for x in x_ticks:
            x_pos = half_width + x * 20  # Scale factor of 20
            painter.drawLine(x_pos, half_height - 5, x_pos, half_height + 5)  # Tick mark
            painter.drawText(x_pos - 8, half_height + 20, str(x))  # Label

        # Draw tick marks and labels on Y-axis
        y_ticks = range(-10, 11)  # Tick marks range from -10 to 10
        for y in y_ticks:
            y_pos = half_height - y * 20  # Scale factor of 20
            painter.drawLine(half_width - 5, y_pos, half_width + 5, y_pos)  # Tick mark
            painter.drawText(half_width + 10, y_pos + 5, str(y))  # Label

        # Plot points and display coordinates
        painter.setPen(QPen(QColor(255, 0, 0), 5))  # Red color, 5-pixel width
        for point in self.points:
            x = half_width + point[0] * 20  # Scale factor of 20
            y = half_height - point[1] * 20  # Scale factor of 20
            painter.drawPoint(x, y)
            painter.drawText(x + 5, y - 5, f"({point[0]}, {point[1]})")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CartesianPlane()
    widget.show()
    sys.exit(app.exec_())
