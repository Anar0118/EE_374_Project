import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400, 300))

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)  # Align contents to the center

        # Create a button
        button = QPushButton("Press Me!")
        button.setFixedSize(QSize(100, 75))  # Set button size

        # Add button to the layout
        layout.addWidget(button)

        # Set layout to the central widget
        central_widget.setLayout(layout)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
