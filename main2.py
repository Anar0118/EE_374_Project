import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                              QLabel, QLineEdit, QComboBox, QPushButton, QTableWidget,
                              QTableWidgetItem, QTabWidget, QGroupBox, QSpinBox, QDoubleSpinBox, QHeaderView)
from PySide6.QtCore import Qt
import math

class Cable:
    def __init__(self, id, code, voltage_level, current_flat, current_trefoil, price_per_meter):
        self.id = id
        self.code = code
        self.voltage_level = voltage_level
        self.current_flat = current_flat
        self.current_trefoil = current_trefoil
        self.price_per_meter = price_per_meter

class PowerCableApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EE374 Power Cable Selection Interface")
        self.setGeometry(100, 100, 1200, 700)
        
        # Initialize cable database (sample data - should be replaced with actual data)
        self.cable_database = [
            Cable(1, "1x10 mm2", "0.6/1 kV", 81, 69, 10),
            Cable(2, "1x16 mm2", "0.6/1 kV", 108, 92, 15),
            Cable(3, "1x25 mm2", "0.6/1 kV", 146, 124, 20),
            Cable(4, "1x35 mm2", "0.6/1 kV", 180, 153, 25),
            Cable(5, "1x50 mm2", "0.6/1 kV", 220, 187, 30),
            Cable(6, "1x70 mm2", "0.6/1 kV", 279, 237, 40),
            Cable(7, "1x95 mm2", "0.6/1 kV", 347, 294, 50),
            Cable(8, "1x120 mm2", "0.6/1 kV", 405, 343, 60),
            Cable(9, "3x16+10 mm2", "0.6/1 kV", None, 89, 45),
            Cable(10, "3x25+16 mm2", "0.6/1 kV", None, 120, 60),
            Cable(11, "3x35+16 mm2", "0.6/1 kV", None, 147, 75),
            Cable(12, "3x50+25 mm2", "0.6/1 kV", None, 179, 90),
            Cable(13, "3x70+35 mm2", "0.6/1 kV", None, 224, 120),
            Cable(14, "3x95+50 mm2", "0.6/1 kV", None, 277, 150),
            Cable(15, "3x120+70 mm2", "0.6/1 kV", None, 323, 180),
            Cable(16, "3x150+70 mm2", "0.6/1 kV", None, 368, 210),
            Cable(17, "1x25 mm2", "3.6/6 kV", 196, 163, 70),
            Cable(18, "1x35 mm2", "3.6/6 kV", 238, 198, 85),
            Cable(19, "1x50 mm2", "3.6/6 kV", 286, 238, 100),
        ]
        
        self.filtered_cables = []
        self.create_toggle_controls()
        self.initUI()
    
    def initUI(self):
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        
        # Create tab widget
        tab_widget = QTabWidget()
        main_layout.addWidget(tab_widget)
        
        # Create tabs
        self.create_input_tab(tab_widget)
        self.create_results_tab(tab_widget)
        
        # Add calculate button
        calculate_btn = QPushButton("Calculate")
        calculate_btn.clicked.connect(self.calculate)
        main_layout.addWidget(calculate_btn)
    
    def create_input_tab(self, tab_widget):
        input_tab = QWidget()
        tab_widget.addTab(input_tab, "Input Parameters")
        
        layout = QVBoxLayout(input_tab)
        
        # Load Specifications Group
        load_group = QGroupBox("Load Specifications")
        load_layout = QVBoxLayout()
        
        # Load Type
        load_type_layout = QHBoxLayout()
        load_type_layout.addWidget(QLabel("Load Type:"))
        self.load_type_combo = QComboBox()
        self.load_type_combo.addItems(["Industrial", "Residential", "Municipal", "Commercial"])
        load_type_layout.addWidget(self.load_type_combo)
        load_layout.addLayout(load_type_layout)
        
        # Voltage Level
        voltage_layout = QHBoxLayout()
        voltage_layout.addWidget(QLabel("Voltage Level (V):"))
        self.voltage_input = QDoubleSpinBox()
        self.voltage_input.setRange(100, 100000)
        self.voltage_input.setValue(400)
        voltage_layout.addWidget(self.voltage_input)
        load_layout.addLayout(voltage_layout)
        
        # Active Power
        active_power_layout = QHBoxLayout()
        active_power_layout.addWidget(QLabel("Active Power (kW):"))
        self.active_power_input = QDoubleSpinBox()
        self.active_power_input.setRange(0.1, 10000)
        self.active_power_input.setValue(100)
        active_power_layout.addWidget(self.active_power_input)
        load_layout.addLayout(active_power_layout)
        
        # Reactive Power
        reactive_power_layout = QHBoxLayout()
        reactive_power_layout.addWidget(QLabel("Reactive Power (kVAR):"))
        self.reactive_power_input = QDoubleSpinBox()
        self.reactive_power_input.setRange(0, 10000)
        self.reactive_power_input.setValue(50)
        reactive_power_layout.addWidget(self.reactive_power_input)
        load_layout.addLayout(reactive_power_layout)
        
        load_group.setLayout(load_layout)
        layout.addWidget(load_group)
        
        # Cable Selection Group
        cable_group = QGroupBox("Cable Selection")
        cable_layout = QVBoxLayout()
        
        # Number of Phase Conductors
        phase_layout = QHBoxLayout()
        phase_layout.addWidget(QLabel("Number of Phase Conductors:"))
        self.phase_combo = QComboBox()
        self.phase_combo.addItems(["1", "3"])
        self.phase_combo.currentTextChanged.connect(self.update_cable_placement)
        phase_layout.addWidget(self.phase_combo)
        cable_layout.addLayout(phase_layout)
        
        # Cable Placement (only for single-phase)
        self.placement_layout = QHBoxLayout()
        self.placement_layout.addWidget(QLabel("Single-core Cable Placement:"))
        self.placement_combo = QComboBox()
        self.placement_combo.addItems(["Flat", "Trefoil"])
        self.placement_layout.addWidget(self.placement_combo)
        self.placement_layout.setEnabled(False)  # Disabled by default (3-phase selected)
        cable_layout.addLayout(self.placement_layout)
        
        cable_group.setLayout(cable_layout)
        layout.addWidget(cable_group)
        
        # Environmental Conditions Group
        env_group = QGroupBox("Environmental Conditions")
        env_layout = QVBoxLayout()
        
        # Trench Information
        trench_layout = QHBoxLayout()
        trench_layout.addWidget(QLabel("Number of Circuits in Trench:"))
        self.trench_spin = QSpinBox()
        self.trench_spin.setRange(1, 4)
        self.trench_spin.setValue(1)
        trench_layout.addWidget(self.trench_spin)
        env_layout.addLayout(trench_layout)
        
        # Environment Temperature
        temp_layout = QHBoxLayout()
        temp_layout.addWidget(QLabel("Environment Temperature (°C):"))
        self.temp_combo = QComboBox()
        self.temp_combo.addItems(["5", "10", "15", "20", "25", "30", "35", "40"])
        self.temp_combo.setCurrentText("20")
        temp_layout.addWidget(self.temp_combo)
        env_layout.addLayout(temp_layout)
        
        # Cable Length
        length_layout = QHBoxLayout()
        length_layout.addWidget(QLabel("Cable Length (m):"))
        self.length_input = QDoubleSpinBox()
        self.length_input.setRange(1, 10000)
        self.length_input.setValue(100)
        length_layout.addWidget(self.length_input)
        env_layout.addLayout(length_layout)
        
        env_group.setLayout(env_layout)
        layout.addWidget(env_group)
        
        # Add stretch to push everything up
        layout.addStretch()
    
    def update_cable_placement(self, text):
        # Enable/disable cable placement based on phase selection
        self.placement_layout.setEnabled(text == "1")
    
    def create_results_tab(self, tab_widget):
        results_tab = QWidget()
        tab_widget.addTab(results_tab, "Results")
        
        layout = QVBoxLayout(results_tab)
        
        # Filtered Cable Table
        self.cable_table = QTableWidget()
        self.cable_table.setColumnCount(10)
        headers = [
            "ID", 
            "Cable Code", 
            "Voltage Level", 
            "Current (A) (Flat)", 
            "Current (A) (Trefoil)", 
            "Resistance (ohm/km)", 
            "Inductance (mH/km) (Flat)", 
            "Inductance (mH/km) (Trefoil)", 
            "Capacitance (uF/km)", 
            "Price/m (TL/km)"
        ]
        self.cable_table.setHorizontalHeaderLabels(headers)
        self.cable_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.cable_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)  # ID
        self.cable_table.setColumnWidth(1, 100)  # Cabel Code
        self.cable_table.setColumnWidth(2, 100)  # Voltage Level
        self.cable_table.setColumnWidth(3, 120)  # Current (Flat)
        self.cable_table.setColumnWidth(4, 120)  # Current (Trefoil)
        self.cable_table.setColumnWidth(5, 120)  # Resistance
        self.cable_table.setColumnWidth(6, 130)  # Inductance (Flat)
        self.cable_table.setColumnWidth(7, 130)  # Inductance (Trefoil)
        self.cable_table.setColumnWidth(8, 120)  # Capacitance
        self.cable_table.setColumnWidth(9, 100)  # Price


        layout.addWidget(QLabel("Available Cables After Filtering:"))
        layout.addWidget(self.cable_table)
        
        # Calculation Results Group
        results_group = QGroupBox("Calculation Results")
        results_layout = QVBoxLayout()
        
        # Line Losses
        losses_layout = QHBoxLayout()
        losses_layout.addWidget(QLabel("Active Power Losses (kW):"))
        self.active_loss_label = QLabel("")
        losses_layout.addWidget(self.active_loss_label)
        results_layout.addLayout(losses_layout)
        
        losses_layout = QHBoxLayout()
        losses_layout.addWidget(QLabel("Reactive Power Losses (kVAR):"))
        self.reactive_loss_label = QLabel("")
        losses_layout.addWidget(self.reactive_loss_label)
        results_layout.addLayout(losses_layout)
        
        # Voltage Regulation
        voltage_reg_layout = QHBoxLayout()
        voltage_reg_layout.addWidget(QLabel("Voltage Regulation (%):"))
        self.voltage_reg_label = QLabel("")
        voltage_reg_layout.addWidget(self.voltage_reg_label)
        results_layout.addLayout(voltage_reg_layout)
        
        # Economic Analysis
        economic_layout = QHBoxLayout()
        economic_layout.addWidget(QLabel("10-Year Cost of Line Losses (TL):"))
        self.loss_cost_label = QLabel("")
        economic_layout.addWidget(self.loss_cost_label)
        results_layout.addLayout(economic_layout)
        
        economic_layout = QHBoxLayout()
        economic_layout.addWidget(QLabel("Cable Installation Cost (TL):"))
        self.install_cost_label = QLabel("")
        economic_layout.addWidget(self.install_cost_label)
        results_layout.addLayout(economic_layout)
        
        economic_layout = QHBoxLayout()
        economic_layout.addWidget(QLabel("Total 10-Year Cost (TL):"))
        self.total_cost_label = QLabel("")
        economic_layout.addWidget(self.total_cost_label)
        results_layout.addLayout(economic_layout)
        
        results_group.setLayout(results_layout)
        layout.addWidget(results_group)
        
        # Selected Cable Info
        selected_layout = QHBoxLayout()
        selected_layout.addWidget(QLabel("Selected Cable:"))
        self.selected_cable_combo = QComboBox()
        selected_layout.addWidget(self.selected_cable_combo)
        layout.addLayout(selected_layout)
        
        # Add stretch to push everything up
        layout.addStretch()
    
    

    def create_toggle_controls(self):
        """Create master toggle button and connect it to all input widgets"""
        self.toggle_button = QPushButton("Disable All Inputs", self)
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self.toggle_all_inputs)
        
        # Add to main layout (assuming you have a main_layout)
        #self.centralWidget().layout().insertWidget(0, self.toggle_button)  # Add at top
        
        # List of all input widgets to toggle
        self.input_widgets = [
            self.load_type_combo,
            self.voltage_input,
            self.active_power_input,
            self.reactive_power_input,
            self.phase_combo,
            self.placement_combo,
            self.trench_spin,
            self.temp_combo,
            self.length_input,
            self.selected_cable_combo
        ]
    
    def toggle_all_inputs(self, checked):
        """Toggle state of all input widgets"""
        for widget in self.input_widgets:
            widget.setEnabled(not checked)
        
        # Update button text
        self.toggle_button.setText("Enable All Inputs" if checked else "Disable All Inputs")
        
        # Special case for placement combo - only enable if phase is 1
        if self.phase_combo.currentText() == "1":
            self.placement_combo.setEnabled(not checked)
        else:
            self.placement_combo.setEnabled(False)

    def calculate(self):
        # Get input values
        load_type = self.load_type_combo.currentText()
        voltage = self.voltage_input.value()
        active_power = self.active_power_input.value() * 1000  # Convert to W
        reactive_power = self.reactive_power_input.value() * 1000  # Convert to VAR
        num_phases = int(self.phase_combo.currentText())
        placement = self.placement_combo.currentText() if num_phases == 1 else None
        num_circuits = self.trench_spin.value()
        temperature = int(self.temp_combo.currentText())
        length = self.length_input.value()
        
        # Calculate load current
        apparent_power = math.sqrt(active_power**2 + reactive_power**2)
        if num_phases == 1:
            current = apparent_power / voltage
        else:  # 3-phase
            current = apparent_power / (math.sqrt(3) * voltage)
        
        # Apply temperature correction
        temp_correction = self.get_temperature_correction(temperature)
        
        # Apply trench reduction
        trench_reduction = self.get_trench_reduction(num_circuits)
        
        # Filter cables based on voltage level
        voltage_filtered = self.filter_by_voltage(voltage)
        
        # Filter cables based on current capacity
        self.filtered_cables = self.filter_by_current(voltage_filtered, current, num_phases, placement, 
                                                    temp_correction, trench_reduction)
        
        # Update cable table
        self.update_cable_table()
        
        # Update selected cable combo
        self.selected_cable_combo.clear()
        for cable in self.filtered_cables:
            self.selected_cable_combo.addItem(f"{cable.id}: {cable.code}", cable.id)
        
        # If we have filtered cables, perform calculations for the first one
        if self.filtered_cables:
            self.perform_calculations(self.filtered_cables[0], current, length, load_type)
    
    def get_temperature_correction(self, temperature):
        # Table 1 from project definition
        corrections = {
            5: 1.15,
            10: 1.10,
            15: 1.05,
            20: 1.00,
            25: 0.95,
            30: 0.90,
            35: 0.85,
            40: 0.80
        }
        return corrections.get(temperature, 1.0)
    
    def get_trench_reduction(self, num_circuits):
        # Table 2 from project definition
        reductions = {
            1: 1.00,
            2: 0.90,
            3: 0.85,
            4: 0.80,
            5: 0.75,
            6: 0.70
        }
        return reductions.get(num_circuits, 1.0)
    
    def filter_by_voltage(self, voltage):
        # Convert voltage to kV for comparison
        voltage_kV = voltage / 1000
        
        filtered = []
        for cable in self.cable_database:
            # Parse voltage level (format: "0.6/1 kV" or "3.6/6 kV")
            try:
                parts = cable.voltage_level.split()
                voltage_parts = parts[0].split('/')
                v_ln = float(voltage_parts[0])  # line-to-neutral
                v_ll = float(voltage_parts[1])  # line-to-line
                
                # For single-phase, compare with line-to-line voltage
                # For three-phase, compare with line-to-line voltage
                if voltage_kV <= v_ll * 1.1:  # Allow 10% tolerance
                    filtered.append(cable)
            except:
                continue
        
        return filtered
    
    def filter_by_current(self, cables, required_current, num_phases, placement, temp_correction, trench_reduction):
        filtered = []
        
        for cable in cables:
            # Determine current capacity based on cable type and placement
            if num_phases == 1:  # Single-phase, single-core cables
                if placement == "Flat" and cable.current_flat is not None:
                    capacity = cable.current_flat
                elif placement == "Trefoil" and cable.current_trefoil is not None:
                    capacity = cable.current_trefoil
                else:
                    continue  # Skip if no capacity for this placement
            else:  # Three-phase cables
                if cable.current_trefoil is not None:  # Three-core cables use trefoil column
                    capacity = cable.current_trefoil
                else:
                    continue  # Skip single-core cables when three-phase is selected
            
            # Apply corrections
            corrected_capacity = capacity * temp_correction * trench_reduction
            
            # Check if capacity is sufficient
            if corrected_capacity >= required_current:
                filtered.append(cable)
        
        return filtered
    
    def update_cable_table(self):
        self.cable_table.setRowCount(len(self.filtered_cables))
        
        for row, cable in enumerate(self.filtered_cables):
            self.cable_table.setItem(row, 0, QTableWidgetItem(str(cable.id)))
            self.cable_table.setItem(row, 1, QTableWidgetItem(cable.code))
            self.cable_table.setItem(row, 2, QTableWidgetItem(cable.voltage_level))
            
            # Display current capacity based on cable type
            if cable.current_flat is not None and cable.current_trefoil is not None:
                current_str = f"Flat: {cable.current_flat}A, Trefoil: {cable.current_trefoil}A"
            else:
                current_str = f"{cable.current_trefoil}A"
            
            self.cable_table.setItem(row, 3, QTableWidgetItem(current_str))
            self.cable_table.setItem(row, 4, QTableWidgetItem(f"{cable.price_per_meter:.2f}"))
        
        self.cable_table.resizeColumnsToContents()
    
    def perform_calculations(self, cable, current, length, load_type):
        # Simplified calculations - these should be replaced with actual formulas from the course
        
        # Calculate resistance (simplified - in reality should come from cable specs)
        resistance = 0.1 * (1000 / length)  # Ω/km -> Ω/m * length
        
        # Line losses (active and reactive)
        active_loss = 3 * (current ** 2) * resistance * length  # 3-phase assumed
        reactive_loss = active_loss * 0.1  # Simplified - should use actual reactance
        
        # Voltage regulation (simplified)
        voltage_regulation = (current * resistance * length * 100) / (self.voltage_input.value() / math.sqrt(3))
        
        # Economic analysis
        operation_hours = {
            "Industrial": 10,
            "Residential": 5,
            "Municipal": 12,
            "Commercial": 8
        }.get(load_type, 8)
        
        days_per_year = 365
        years = 10
        electricity_price = 2.5  # TL/kWh (2500 TL/MWh)
        
        # Cost of line losses
        loss_cost = (active_loss / 1000) * operation_hours * days_per_year * years * electricity_price
        
        # Installation cost
        install_cost = cable.price_per_meter * length
        
        # Update UI
        self.active_loss_label.setText(f"{active_loss / 1000:.2f}")
        self.reactive_loss_label.setText(f"{reactive_loss / 1000:.2f}")
        self.voltage_reg_label.setText(f"{voltage_regulation:.2f}")
        self.loss_cost_label.setText(f"{loss_cost:,.2f}")
        self.install_cost_label.setText(f"{install_cost:,.2f}")
        self.total_cost_label.setText(f"{loss_cost + install_cost:,.2f}")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PowerCableApp()
    window.show()
    sys.exit(app.exec())