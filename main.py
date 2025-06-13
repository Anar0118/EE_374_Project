import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                              QLabel, QLineEdit, QComboBox, QPushButton, QTableWidget,
                              QTableWidgetItem, QTabWidget, QGroupBox, QSpinBox, QDoubleSpinBox, QHeaderView, QScrollArea,QMessageBox)
from PySide6.QtCore import Qt
import math

class Cable:
    def __init__(self, id, code, voltage_level, current_flat, current_trefoil, resistance, inductance_flat, inductance_trefoil, capacitance, price_per_meter):
        self.id = id
        self.code = code
        self.voltage_level = voltage_level
        self.current_flat = current_flat
        self.current_trefoil = current_trefoil
        self.resistance = resistance
        self.inductance_flat = inductance_flat
        self.inductance_trefoil = inductance_trefoil
        self.capacitance = capacitance
        self.price_per_meter = price_per_meter

class PowerCableApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EE374 Power Cable Selection Interface")
        self.setGeometry(100, 100, 1220, 700)
        
        # Initialize cable database (sample data - should be replaced with actual data)
        self.cable_database = [
            Cable(1, "1x10 mm2", "0.6/1 kV", 81, 69, 1.83, 0.34, 0.41, None, 102300),
            Cable(2, "1x16 mm2", "0.6/1 kV", 108, 92, 1.15, 0.317, 0.387, None, 156600),
            Cable(3, "1x25 mm2", "0.6/1 kV", 146, 124, 0.727, 0.304, 0.374, None, 241400),
            Cable(4, "1x35 mm2", "0.6/1 kV", 180, 153, 0.524, 0.291, 0.36, None, 328300),
            Cable(5, "1x50 mm2", "0.6/1 kV", 220, 187, 0.387, 0.281, 0.351, None, 434000),
            Cable(6, "1x70 mm2", "0.6/1 kV", 279, 237, 0.268, 0.272, 0.341, None, 623000),
            Cable(7, "1x95 mm2", "0.6/1 kV", 347, 294, 0.193, 0.264, 0.333, None, 847000),
            Cable(8, "1x120 mm2", "0.6/1 kV", 405, 343, 0.153, 0.259, 0.329, None, 1080000),
            Cable(9, "3x16+10 mm2", "0.6/1 kV", None, 89, 1.15, None, 0.264, None, 640000),
            Cable(10, "3x25+16 mm2", "0.6/1 kV", None, 120, 0.727, None, 0.265, None, 990000),
            Cable(11, "3x35+16 mm2", "0.6/1 kV", None, 147, 0.524, None, 0.258, None, 1300000),
            Cable(12, "3x50+25 mm2", "0.6/1 kV", None, 179, 0.387, None, 0.256, None, 1750000),
            Cable(13, "3x70+35 mm2", "0.6/1 kV", None, 224, 0.268, None, 0.253, None, 2520000),
            Cable(14, "3x95+50 mm2", "0.6/1 kV", None, 277, 0.193, None, 0.247, None, 3400000),
            Cable(15, "3x120+70 mm2", "0.6/1 kV", None, 323, 0.153, None, 0.246, None, 4400000),
            Cable(16, "3x150+70 mm2", "0.6/1 kV", None, 368, 0.124, None, 0.248, None, 5200000),
            Cable(17, "1x25 mm2", "3.6/6 kV", 196, 163, 0.727, 0.77, 0.43, 0.25, 351000),
            Cable(18, "1x35 mm2", "3.6/6 kV", 238, 198, 0.524, 0.75, 0.41, 0.28, 532000),
            Cable(19, "1x50 mm2", "3.6/6 kV", 286, 238, 0.387, 0.72, 0.39, 0.31, 638000),
            Cable(20, "1x70 mm2", "3.6/6 kV", 356, 296, 0.268, 0.68, 0.37, 0.36, 825000),
            Cable(21, "1x95 mm2", "3.6/6 kV", 434, 361, 0.193, 0.65, 0.36, 0.4, 1070000),
            Cable(22, "1x120 mm2", "3.6/6 kV", 600, 417, 0.153, 0.63, 0.34, 0.44, 1300000),
            Cable(23, "1x150 mm2", "3.6/6 kV", 559, 473, 0.124, 0.62, 0.33, 0.48, 1640000),
            Cable(24, "1x185 mm2", "3.6/6 kV", 637, 543, 0.0991, 0.6, 0.32, 0.52, 1950000),
            Cable(25, "3x25+16 mm2", "3.6/6 kV", None, 143, 0.727, None, 0.37, 0.25, 1647000),
            Cable(26, "3x35+16 mm2", "3.6/6 kV", None, 172, 0.524, None, 0.35, 0.28, 2002000),
            Cable(27, "3x50+16 mm2", "3.6/6 kV", None, 205, 0.387, None, 0.34, 0.3, 2594000),
            Cable(28, "3x70+16 mm2", "3.6/6 kV", None, 253, 0.268, None, 0.32, 0.35, 3450000),
            Cable(29, "3x95+16 mm2", "3.6/6 kV", None, 307, 0.193, None, 0.31, 0.39, 4727000),
            Cable(30, "3x120+16 mm2", "3.6/6 kV", None, 352, 0.153, None, 0.3, 0.43, 5784000),
            Cable(31, "3x150+25 mm2", "3.6/6 kV", None, 397, 0.124, None, 0.29, 0.47, 6963000),
            Cable(32, "3x185+25 mm2", "3.6/6 kV", None, 453, 0.0991, None, 0.28, 0.5, 8481000),
            Cable(33, "1x35 mm2", "6/10 kV", 231, 195, 0.524, 0.661, 0.383, 0.223, 785100),
            Cable(34, "1x50 mm2", "6/10 kV", 277, 234, 0.387, 0.636, 0.366, 0.248, 944900),
            Cable(35, "1x70 mm2", "6/10 kV", 345, 292, 0.268, 0.606, 0.349, 0.285, 1226000),
            Cable(36, "1x95 mm2", "6/10 kV", 418, 354, 0.193, 0.582, 0.334, 0.32, 1533000),
            Cable(37, "1x120 mm2", "6/10 kV", 481, 407, 0.153, 0.563, 0.323, 0.35, 1872000),
            Cable(38, "1x150 mm2", "6/10 kV", 537, 460, 0.124, 0.546, 0.313, 0.382, 2362000),
            Cable(39, "1x185 mm2", "6/10 kV", 612, 527, 0.0991, 0.529, 0.304, 0.415, 2838000),
            Cable(40, "3x35 mm2", "6/10 kV", None, 173, 0.524, None, 0.374, 0.189, 2127000),
            Cable(41, "3x50 mm2", "6/10 kV", None, 206, 0.387, None, 0.355, 0.209, 2716000),
            Cable(42, "3x70 mm2", "6/10 kV", None, 257, 0.268, None, 0.336, 0.236, 3603000),
            Cable(43, "3x95 mm2", "6/10 kV", None, 313, 0.193, None, 0.32, 0.263, 4901000),
            Cable(44, "3x120 mm2", "6/10 kV", None, 360, 0.153, None, 0.308, 0.291, 5934000),
            Cable(45, "3x150 mm2", "6/10 kV", None, 410, 0.124, None, 0.299, 0.314, 7125000),
            Cable(46, "3x185 mm2", "6/10 kV", None, 469, 0.0991, None, 0.29, 0.341, 8659000),
            Cable(47, "1x95 mm2", "12/20 kV", 420, 358, 0.193, 0.59, 0.36, 0.218, 1560000),
            Cable(48, "1x120 mm2", "12/20 kV", 483, 412, 0.153, 0.571, 0.349, 0.238, 1906000),
            Cable(49, "1x150 mm2", "12/20 kV", 540, 466, 0.124, 0.554, 0.338, 0.258, 2393000),
            Cable(50, "1x185 mm2", "12/20 kV", 614, 534, 0.0991, 0.538, 0.329, 0.278, 2877000),
            Cable(51, "1x240 mm2", "12/20 kV", 718, 627, 0.0754, 0.518, 0.317, 0.308, 3543000),
            Cable(52, "1x300 mm2", "12/20 kV", 813, 715, 0.0601, 0.501, 0.308, 0.336, 4455000),
            Cable(53, "1x400 mm2", "12/20 kV", 904, 819, 0.047, 0.48, 0.298, 0.377, 5669000),
            Cable(54, "1x150 mm2", "20.3/35 kV", 559, 473, 0.124, 0.64, 0.41, 0.17, 1720000),
            Cable(55, "1x185 mm2", "20.3/35 kV", 637, 543, 0.0991, 0.63, 0.39, 0.18, 2020000),
            Cable(56, "1x240 mm2", "20.3/35 kV", 745, 641, 0.0754, 0.6, 0.38, 0.2, 2530000),
            Cable(57, "1x300 mm2", "20.3/35 kV", 846, 735, 0.0601, 0.59, 0.37, 0.21, 3150000),
            Cable(58, "1x400 mm2", "20.3/35 kV", 938, 845, 0.047, 0.57, 0.35, 0.23, 4100000),
            Cable(59, "1x500 mm2", "20.3/35 kV", 1010, 950, 0.0366, 0.55, 0.34, 0.26, 5150000),
            Cable(60, "1x630 mm2", "20.3/35 kV", 1120, 1040, 0.0283, 0.52, 0.33, 0.29, 6550000),
            Cable(61, "3x95 mm2", "20.3/35 kV", None, 307, 0.193, None, 0.4, 0.15, 4600000),
            Cable(62, "3x120 mm2", "20.3/35 kV", None, 352, 0.153, None, 0.39, 0.16, 5500000),
            Cable(63, "3x150 mm2", "20.3/35 kV", None, 397, 0.124, None, 0.37, 0.17, 6400000),
            Cable(64, "3x185 mm2", "20.3/35 kV", None, 453, 0.0991, None, 0.36, 0.18, 7500000),
            Cable(65, "3x240 mm2", "20.3/35 kV", None, 529, 0.0754, None, 0.35, 0.2, 9400000),
            Cable(66, "3x300 mm2", "20.3/35 kV", None, 626, 0.0601, None, 0.29, 0.22, 11300000),
            Cable(67, "3x400 mm2", "20.3/35 kV", None, 720, 0.047, None, 0.28, 0.24, 14300000)
        ]
        
        self.filtered_cables = []
        
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
        self.create_info_tab(tab_widget)
        
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
        self.voltage_input.setRange(0, 100000)
        self.voltage_input.setValue(400)
        voltage_layout.addWidget(self.voltage_input)
        load_layout.addLayout(voltage_layout)
        
        # Add note below Voltage Level
        voltage_note_label = QLabel("Note: Enter 0 to ignore voltage filtering and list all cables")
        voltage_note_label.setStyleSheet("font-style: italic; color: #DC143C; font-size: 9pt;")
        load_layout.addWidget(voltage_note_label)

        # Active Power
        active_power_layout = QHBoxLayout()
        active_power_layout.addWidget(QLabel("Active Power (kW):"))
        self.active_power_input = QDoubleSpinBox()
        self.active_power_input.setRange(0, 100000)
        self.active_power_input.setValue(0)
        active_power_layout.addWidget(self.active_power_input)
        load_layout.addLayout(active_power_layout)

        # Add note below Active Power
        active_power_note_label = QLabel("Note: Enter 0 for both Active and Reactive Power to ignore current filtering")
        active_power_note_label.setStyleSheet("font-style: italic; color: #DC143C; font-size: 9pt;")
        load_layout.addWidget(active_power_note_label)


        # Reactive Power
        reactive_power_layout = QHBoxLayout()
        reactive_power_layout.addWidget(QLabel("Reactive Power (kVAR):"))
        self.reactive_power_input = QDoubleSpinBox()
        self.reactive_power_input.setRange(0, 100000)
        self.reactive_power_input.setValue(0)
        reactive_power_layout.addWidget(self.reactive_power_input)
        load_layout.addLayout(reactive_power_layout)
        
        # Add note below Reactive Power
        reactive_power_note_label = QLabel("Note: Enter 0 for both Active and Reactive Power to ignore current filtering")
        reactive_power_note_label.setStyleSheet("font-style: italic; color: #DC143C; font-size: 9pt;")
        load_layout.addWidget(reactive_power_note_label)

        load_group.setLayout(load_layout)
        layout.addWidget(load_group)
        
        # Cable Selection Group
        cable_group = QGroupBox("Cable Selection")
        cable_layout = QVBoxLayout()
        
        # Number of Cores in Phase Conductors
        phase_layout = QHBoxLayout()
        phase_layout.addWidget(QLabel("Number of Cores in Phase Conductors:"))
        self.phase_combo = QComboBox()
        self.phase_combo.addItems(["None","1", "3"])
        self.phase_combo.currentTextChanged.connect(self.update_cable_placement)
        phase_layout.addWidget(self.phase_combo)
        cable_layout.addLayout(phase_layout)
        
        # Add note below Number of Cores
        cores_note_label = QLabel("Note: Enter None to list both 1 and 3 core options")
        cores_note_label.setStyleSheet("font-style: italic; color: #DC143C; font-size: 9pt;")
        cable_layout.addWidget(cores_note_label)
        
        # Cable Placement (only for single-phase)
        self.placement_layout = QHBoxLayout()
        self.placement_layout.addWidget(QLabel("Single-core Cable Placement:"))
        self.placement_combo = QComboBox()
        self.placement_combo.addItems(["Flat", "Trefoil"])
        self.placement_layout.addWidget(self.placement_combo)
        self.placement_layout.setEnabled(True)  # Disabled by default (3-phase selected)
        cable_layout.addLayout(self.placement_layout)
        
        # Add note below Cable Placement
        placements_note_label = QLabel("Note: Cable Placement is functional only if Number of Cores is 1")
        placements_note_label.setStyleSheet("font-style: italic; color: #DC143C; font-size: 9pt;")
        cable_layout.addWidget(placements_note_label)

        cable_group.setLayout(cable_layout)
        layout.addWidget(cable_group)
        
        # Environmental Conditions Group
        env_group = QGroupBox("Environmental Conditions")
        env_layout = QVBoxLayout()
        
        # Trench Information
        trench_layout = QHBoxLayout()
        trench_layout.addWidget(QLabel("Number of Circuits in Trench:"))
        self.trench_combo_box = QComboBox()
        self.trench_combo_box.addItems(["1","2","3","4","5","6"])
        trench_layout.addWidget(self.trench_combo_box)
        env_layout.addLayout(trench_layout)

        # Add note below Trench Number
        trench_number_nore_label = QLabel("Limits: For Single Core Cable choose 1-2\n" \
        "For 3 Core Cable choose 1-6")
        trench_number_nore_label.setStyleSheet("font-style: italic; color: #DC143C; font-size: 9pt;")
        env_layout.addWidget(trench_number_nore_label)
        
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
        self.length_input.setRange(1, 1000000)
        self.length_input.setValue(100)
        length_layout.addWidget(self.length_input)
        env_layout.addLayout(length_layout)

        env_group.setLayout(env_layout)
        layout.addWidget(env_group)
        
        # Current Information Group
        current_group = QGroupBox("Current Information")
        current_layout = QVBoxLayout()
        
        # Required Current
        req_current_layout = QHBoxLayout()
        req_current_layout.addWidget(QLabel("Required Current (A):"))
        self.required_current_label = QLabel("")
        req_current_layout.addWidget(self.required_current_label)
        current_layout.addLayout(req_current_layout)
        
        # Updated Current (after corrections)
        updated_current_layout = QHBoxLayout()
        updated_current_layout.addWidget(QLabel("Updated Current (A):"))
        self.updated_current_label = QLabel("")
        updated_current_layout.addWidget(self.updated_current_label)
        current_layout.addLayout(updated_current_layout)
        
        current_group.setLayout(current_layout)
        layout.addWidget(current_group)
        
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
        self.cable_table.setColumnWidth(5, 140)  # Resistance
        self.cable_table.setColumnWidth(6, 150)  # Inductance (Flat)
        self.cable_table.setColumnWidth(7, 165)  # Inductance (Trefoil)
        self.cable_table.setColumnWidth(8, 140)  # Capacitance
        self.cable_table.setColumnWidth(9, 100)  # Price


        layout.addWidget(QLabel("Available Cables After Filtering:"))
        layout.addWidget(self.cable_table)
        
        # Calculation Results Group
        self.results_group = QGroupBox("Calculation Results")
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
        
        self.results_group.setLayout(results_layout)
        layout.addWidget(self.results_group)
        
        # Selected Cable Info
        selected_layout = QHBoxLayout()
        selected_layout.addWidget(QLabel("Selected Cable:"))
        self.selected_cable_combo = QComboBox()
        selected_layout.addWidget(self.selected_cable_combo)
        layout.addLayout(selected_layout)


        # Add Calculate Selected button
        self.calculate_selected_btn = QPushButton("Calculate Selected Cable")
        self.calculate_selected_btn.clicked.connect(self.calculate_selected_cable)
        layout.addWidget(self.calculate_selected_btn)
        
        # Add stretch to push everything up
        layout.addStretch()
    
    def create_info_tab(self, tab_widget):
        info_tab = QWidget()
        tab_widget.addTab(info_tab, "INFO")

        # Create scroll area for the info tab
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        scroll.setWidget(content)
        
        # Main layout for the content
        layout = QVBoxLayout(content)
        
        # Application Title
        title = QLabel("Power Cable Selection Interface")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 15px;")
        layout.addWidget(title)
        
        # Description
        desc = QLabel(
            "This application helps select appropriate power cables based on:\n"
            "- Load specifications\n"
            "- Environmental conditions\n"
            "- Technical requirements\n\n"
            "Course: EE374 - Fundamentals of Power Systems and Electrical Equipment"
        )
        desc.setAlignment(Qt.AlignCenter)
        desc.setWordWrap(True)
        layout.addWidget(desc)
        
        # Usage Instructions
        usage_group = QGroupBox("How To Use")
        usage_layout = QVBoxLayout()
        
        instructions = [
            ("1. Input Parameters", "Enter all required parameters in the Input tab"),
            ("2. Special Cases", 
            "• Set voltage = 0 to disable voltage filtering and list all available cables\n"
            "• Set both active and reactive powers = 0 to disable current filtering"),
            ("3. Results", "View filtered cables and their specifications"),
            ("4. Analysis", "Check voltage regulation and economic factors (Not functional until Phase-2)")
        ]
        
        for header, text in instructions:
            header_label = QLabel(header)
            header_label.setStyleSheet("font-weight: bold;")
            usage_layout.addWidget(header_label)
            
            text_label = QLabel(text)
            text_label.setStyleSheet("margin-left: 10px;")
            text_label.setWordWrap(True)
            usage_layout.addWidget(text_label)
            usage_layout.addSpacing(5)
        
        usage_group.setLayout(usage_layout)
        layout.addWidget(usage_group)
        
        # Quick Tips
        tips_group = QGroupBox("Quick Tips")
        tips_layout = QVBoxLayout()
        
        tips = [
            "• For better experience:\n"
            "   1)Give values to parameters in Input Tab\n"
            "   2)Switch to Results Tab\n"
            "   3)And then, press Calculate button",
            "• None value in Number of Cores will list cables regardless of their core numbers",
            "• Single Core Cable Placement is only functional when Number of Cores is 1",
            "• For 1 core cables choose Number of Circuits in Trench from 1 to 2",
            "• For 3 core cables choose Number of Circuits in Trench from 1 to 6",
            "• Load Type and Cable Length is not functional until Phase-2"
        ]
        
        for tip in tips:
            tip_label = QLabel(f"{tip}")
            tip_label.setWordWrap(True)
            tips_layout.addWidget(tip_label)
        
        tips_group.setLayout(tips_layout)
        layout.addWidget(tips_group)

        # Future Updates
        updates_group = QGroupBox("Future Updates")
        updates_layout = QVBoxLayout()
        
        updates = [
            "Will:",
            "• try to make dynamic layout changes",
            "• add economic analysis based on selected cable from filtered list"
        ]
        
        for update in updates:
            update_label = QLabel(f"{update}")
            update_label.setWordWrap(True)
            updates_layout.addWidget(update_label)
        
        updates_group.setLayout(updates_layout)
        layout.addWidget(updates_group)
        
        # Add stretch to push content up
        layout.addStretch()
        
        # Set the scroll area as the info tab's layout
        info_layout = QVBoxLayout(info_tab)
        info_layout.addWidget(scroll)
        
    def calculate(self):
        # Get input values
        load_type = self.load_type_combo.currentText()
        voltage = self.voltage_input.value()
        active_power = self.active_power_input.value() * 1000  # Convert to W
        reactive_power = self.reactive_power_input.value() * 1000  # Convert to VAR
        if self.phase_combo.currentText() == "None":
            num_cores = None
        else: 
            num_cores = int(self.phase_combo.currentText())
        
        placement = self.placement_combo.currentText() if num_cores == 1 else None
        num_circuits = int(self.trench_combo_box.currentText())
        temperature = int(self.temp_combo.currentText())
        length = self.length_input.value()
        
        # Calculate load current
        apparent_power = math.sqrt(active_power**2 + reactive_power**2)
        #if 
        if voltage == 0:
            current = 0
        else:
            current = apparent_power / (math.sqrt(3) * voltage)
        
        self.required_current_label.setText(f"{current:.2f}")
        
        # Apply temperature correction
        temp_correction = self.get_temperature_correction(temperature)
        
        #updated_current = current / temp_correction

        # Apply trench reduction
        if num_cores == 1:
            trench_reduction = self.get_trench_reduction(num_circuits*3)
        elif num_cores == 3:
            trench_reduction = self.get_trench_reduction(num_circuits)
        else:
            trench_reduction = self.get_trench_reduction(1)

        
        # Filter cables based on voltage level
        voltage_filtered = self.filter_by_voltage(voltage)
        
        # Filter cables based on current capacity
        self.filtered_cables = self.filter_by_current(voltage_filtered, current, num_cores, placement, 
                                                      temp_correction, trench_reduction, num_circuits)
        
        # Update cable table
        self.update_cable_table()
        
        # Update selected cable combo
        self.selected_cable_combo.clear()
        for cable in self.filtered_cables:
            self.selected_cable_combo.addItem(f"{cable.id}: {cable.code}", cable.id)


        self.selected_cable_combo.clear()
        for cable in self.filtered_cables:
            self.selected_cable_combo.addItem(f"{cable.id}: {cable.code}", cable.id)
        
        # Calculate for first cable if available
        if self.filtered_cables:
            self.selected_cable_combo.setCurrentIndex(0)
            self.calculate_selected_cable()
        else:
            self.show_no_cables_warning()
        
        '''
        # If we have filtered cables, perform calculations for the first one
        if self.filtered_cables:
            self.perform_calculations(self.filtered_cables[0], current, length, load_type)

        if not self.filtered_cables:
            self.show_no_cables_warning()
            return
        '''
    
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
        if voltage == 0: # No Filtering
            return self.cable_database
        
        # Convert voltage to kV for comparison
        voltage_kV = voltage / 1000
        voltage_list = [1,6,10,20,35]
        filtered = []
        for cable in self.cable_database:
            # Parse voltage level (format: "0.6/1 kV" or "3.6/6 kV")
            try:
                parts = cable.voltage_level.split()
                voltage_parts = parts[0].split('/')
                v_ln = float(voltage_parts[0])  # line-to-neutral
                v_ll = float(voltage_parts[1])  # line-to-line

                max_limit = None
                for voltage in sorted(voltage_list):
                    if voltage_kV <= voltage:
                        max_limit = voltage
                        break
                
                # Only include cable if:
                # 1. Input voltage <= cable's line-to-line voltage AND
                # 2. Cable's voltage is <= the next standard voltage level (or is the highest)
                if voltage_kV <= v_ll and (max_limit is None or v_ll <= max_limit):
                    filtered.append(cable)
            except Exception as e:
                print(f"Skipping cable {cable.id}: Invalid voltage format '{cable.voltage_level}'")
                continue
        
        return filtered
    
    def filter_by_current(self, cables, required_current, num_cores, placement, temp_correction, trench_reduction, num_circuits):
        if required_current == 0:  # No current filtering
            return cables
            
        filtered = []
        
        for cable in cables:
            # Skip if cable doesn't match core requirements
            cable_cores = self._get_cable_core_count(cable.code)
            if (num_cores is not None) and (cable_cores != num_cores):
                continue
                
            # Determine current capacity
            capacity = self._get_cable_capacity(cable, num_cores, placement)
            if capacity is None:
                continue
                
            # Apply corrections
            updated_current = required_current / (temp_correction * trench_reduction * num_circuits)
            self.updated_current_label.setText(f"{updated_current:.2f}")
            
            
            if updated_current <= capacity:
                filtered.append(cable)
        
        return filtered
    
    def update_cable_table(self):
        if not self.filtered_cables:
            self.cable_table.setRowCount(1)
            self.cable_table.setItem(0, 0, QTableWidgetItem("No cables found"))
            self.cable_table.item(0, 0).setTextAlignment(Qt.AlignCenter)
            # Merge columns for the message
            self.cable_table.setSpan(0, 0, 1, self.cable_table.columnCount())
            return
        self.cable_table.setRowCount(len(self.filtered_cables))
        
        def format_value(value, unit="", decimals=2):
            """Helper function to handle None values and formatting"""
            if value is None:
                return "-"
            if isinstance(value, str):
                return value
            return f"{value:.{decimals}f}{unit}"
    
        for row, cable in enumerate(self.filtered_cables):
            # Create centered items with unified None handling
            def create_item(value, unit="", decimals=2):
                item = QTableWidgetItem(format_value(value, unit, decimals))
                item.setTextAlignment(Qt.AlignCenter)
                return item
            
            # Set items for each column
            self.cable_table.setItem(row, 0, create_item(cable.id,"",0))
            self.cable_table.setItem(row, 1, create_item(cable.code))
            self.cable_table.setItem(row, 2, create_item(cable.voltage_level))
            self.cable_table.setItem(row, 3, create_item(cable.current_flat, "A", 0))
            self.cable_table.setItem(row, 4, create_item(cable.current_trefoil, "A", 0))
            self.cable_table.setItem(row, 5, create_item(cable.resistance, " Ω/km", 4))
            self.cable_table.setItem(row, 6, create_item(cable.inductance_flat, " mH/km", 4))
            self.cable_table.setItem(row, 7, create_item(cable.inductance_trefoil, " mH/km", 4))
            self.cable_table.setItem(row, 8, create_item(cable.capacitance, " μF/km", 6))
            self.cable_table.setItem(row, 9, create_item(cable.price_per_meter, " TL", 2))
        
        self.cable_table.resizeColumnsToContents()
    
    def _get_cable_core_count(self, cable_code):
        """Extract core count from cable code (e.g., '3x150+70 mm2' → 3)"""
        if 'x' in cable_code:
            return int(cable_code.split('x')[0])
        return 1  # Default to single-core if no 'x' in code
    
    def _get_cable_capacity(self, cable, num_cores, placement):
        """Get appropriate current capacity based on cable type and placement"""
        if num_cores == 1:  # Single-core
            if placement == "Flat":
                return cable.current_flat
            return cable.current_trefoil
        else:  # Multi-core (3 or 4)
            return cable.current_trefoil
        
    def _get_cable_inductance(self, cable, num_cores, placement):
        """Get appropriate current capacity based on cable type and placement"""
        if num_cores == 1:  # Single-core
            if placement == "Flat":
                return cable.inductance_flat
            return cable.inductance_trefoil
        else:  # Multi-core (3 or 4)
            return cable.inductance_trefoil
    
    def show_no_cables_warning(self):
        """Display warning when no cables match criteria"""
        warning = QMessageBox()
        warning.setIcon(QMessageBox.Warning)
        warning.setWindowTitle("No Suitable Cables")
        warning.setText("No cables meet the specified requirements.")
        warning.setInformativeText(
            "Please check:\n"
            "• Voltage level\n"
            "• Current requirements\n"
            "• Core type selection\n"
            "• Environmental conditions"
        )
        warning.setStandardButtons(QMessageBox.Ok)
        warning.exec()
        
        # Clear previous results
        self.cable_table.setRowCount(0)
        self.clear_results_display()
    
    def clear_cable_info_label(self):
        """Remove the cable info label if it exists"""
        if hasattr(self, 'cable_info_label') and self.cable_info_label is not None:
            # Remove from layout and delete
            self.results_group.layout().removeWidget(self.cable_info_label)
            self.cable_info_label.deleteLater()
            self.cable_info_label = None

    def clear_results_display(self):
        """Reset all result fields"""
        self.active_loss_label.setText("")
        self.reactive_loss_label.setText("")
        self.voltage_reg_label.setText("")
        self.loss_cost_label.setText("")
        self.install_cost_label.setText("")
        self.total_cost_label.setText("")
    
    def perform_calculations(self, cable, current, length, load_type):
        # Clear any previous cable info label first
        self.clear_cable_info_label()
        
        # Add cable info to results
        self.cable_info_label = QLabel(f"Calculations for: {cable.code} ({cable.voltage_level})")
        self.cable_info_label.setStyleSheet("font-weight: bold; color: #E0115F;")
        
        # Insert just above the results group
        self.results_group.layout().insertWidget(0, self.cable_info_label)

        voltage = self.voltage_input.value()

        if self.phase_combo.currentText() == "None":
            num_cores = None
        else: 
            num_cores = int(self.phase_combo.currentText())
        
        if num_cores == 1:
            k = 3
        else: k = 1
        

        # Calculate resistance (simplified - in reality should come from cable specs)
        placement = self.placement_combo.currentText() if num_cores == 1 else None
        num_circuits = int(self.trench_combo_box.currentText())
        length = self.length_input.value()

        resistance = 0.1 * (1000 / length)  # Ω/km -> Ω/m * length
        R_total = (cable.resistance * (length/1000)) / (num_circuits)
        X_total = (self._get_cable_inductance(cable, num_cores, placement) * (length/1000) * (2*math.pi*50)) / ((num_circuits) * 1000)
        
        #print(cable.resistance)
        #print(length)
        #print(num_circuits)
        #print(self._get_cable_inductance(cable, num_cores, placement))
        #print(f"R: {R_total}")
        #print(f"X: {X_total}")
        
        # Line losses (active and reactive) in kW/KVAR
        active_loss = 3 * (current ** 2) * R_total  # 3-phase assumed
        reactive_loss = 3 * (current ** 2) * X_total
        
        # Voltage regulation (simplified)
        voltage_regulation =  ((active_loss * 1000) * R_total - (reactive_loss * 1000) * X_total) / (voltage**2)  #(current * resistance * length * 100) / (self.voltage_input.value() / math.sqrt(3))
        
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
        loss_cost = (active_loss/1000) * operation_hours * days_per_year * years * electricity_price
        
        # Installation cost
        install_cost = cable.price_per_meter * (length/1000) * (num_circuits * k)
        
        # Update UI
        self.active_loss_label.setText(f"{active_loss / 1000:.2f}")
        self.reactive_loss_label.setText(f"{reactive_loss / 1000:.2f}")
        self.voltage_reg_label.setText(f"{voltage_regulation:.2f}")
        self.loss_cost_label.setText(f"{loss_cost:,.2f}")
        self.install_cost_label.setText(f"{install_cost:,.2f}")
        self.total_cost_label.setText(f"{loss_cost + install_cost:,.2f}")
    
    def calculate_selected_cable(self):
        if not self.filtered_cables:
            return
            
        # Get current selection
        selected_index = self.selected_cable_combo.currentIndex()
        if selected_index < 0:  # No selection
            return
            
        selected_cable = self.filtered_cables[selected_index]
        
        # Get input values needed for calculations
        try:
            voltage = self.voltage_input.value()
            active_power = self.active_power_input.value() * 1000  # Convert to W
            reactive_power = self.reactive_power_input.value() * 1000  # Convert to VAR
            length = self.length_input.value()
            load_type = self.load_type_combo.currentText()
            
            # Calculate current (skip if voltage is 0)
            apparent_power = math.sqrt(active_power**2 + reactive_power**2)
            current = apparent_power / (math.sqrt(3) * voltage) if voltage != 0 else 0
            
            # Perform calculations for selected cable
            self.perform_calculations(selected_cable, current, length, load_type)
            
        except Exception as e:
            QMessageBox.warning(self, "Calculation Error", f"Error calculating results: {str(e)}")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PowerCableApp()
    window.show()
    sys.exit(app.exec())