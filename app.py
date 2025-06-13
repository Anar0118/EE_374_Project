from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QTextEdit


class CableSelectionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Power Cable Selection Interface")
        self.setGeometry(100, 100, 500, 400)

        self.load_label = QLabel("Load (kW):")
        self.load_input = QLineEdit()

        self.voltage_label = QLabel("Voltage Level (V):")
        self.voltage_input = QLineEdit()
        
        self.phase_label = QLabel("Phase Conductors:")
        self.phase_input = QComboBox()
        self.phase_input.addItems(["Single-Phase", "Three-Phase"])
        
        self.temp_label = QLabel("Environment Temperature (°C):")
        self.temp_input = QLineEdit()
        
        self.length_label = QLabel("Cable Length (m):")
        self.length_input = QLineEdit()
        
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_selection)
        
        self.result_output = QTextEdit()
        self.result_output.setReadOnly(True)


        layout = QVBoxLayout()
        layout.addWidget(self.load_label)
        layout.addWidget(self.load_input)
        layout.addWidget(self.voltage_label)
        layout.addWidget(self.voltage_input)
        layout.addWidget(self.phase_label)
        layout.addWidget(self.phase_input)
        layout.addWidget(self.temp_label)
        layout.addWidget(self.temp_input)
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_output)
        
        self.setLayout(layout)

    def calculate_selection(self):
        try:
            load = float(self.load_input.text())
            voltage = float(self.voltage_input.text())
            length = float(self.length_input.text())
            temp = float(self.temp_input.text())
            phase = self.phase_input.currentText()
            
            # Placeholder calculation logic (Replace with real formula)
            current = load / voltage  # Simplified formula
            cable_size = "16 mm²" if current < 100 else "25 mm²"  # Example selection
            
            self.result_output.setText(f"Estimated Current: {current:.2f} A\nSuggested Cable Size: {cable_size}")
        except ValueError:
            self.result_output.setText("Invalid input. Please enter numeric values.")



if __name__ == "__main__":
    app = QApplication([])
    window = CableSelectionApp()
    window.show()
    app.exec()