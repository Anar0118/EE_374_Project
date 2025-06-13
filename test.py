import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                              QVBoxLayout, QLabel, QTabWidget)

class WelcomeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Welcome Application")
        self.setGeometry(100, 100, 600, 400)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create tab widget
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        
        # Create welcome tab
        self.create_welcome_tab()
        
        # Optional: Add more tabs if needed
        # self.create_other_tabs()
    
    def create_welcome_tab(self):
        """Create the welcome tab with user greeting"""
        welcome_tab = QWidget()
        tab_layout = QVBoxLayout(welcome_tab)
        
        # Welcome message
        welcome_label = QLabel("<h1>Welcome to Our Application!</h1>")
        welcome_label.setStyleSheet("font-size: 24px; color: #2c3e50;")
        tab_layout.addWidget(welcome_label)
        
        # Additional info
        info_label = QLabel(
            "<p>We're glad to have you here. This application is designed to "
            "help you with your tasks.</p>"
            "<p>Please explore the features and let us know if you need any assistance.</p>"
            "<p>Start by navigating through the tabs above.</p>"
        )
        info_label.setStyleSheet("font-size: 14px; color: #34495e;")
        info_label.setWordWrap(True)
        tab_layout.addWidget(info_label)
        
        # Add some spacing
        tab_layout.addStretch()
        
        # Add the tab to the tab widget
        self.tabs.addTab(welcome_tab, "Welcome")
    
    # You can add more methods to create additional tabs here

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set a modern style
    app.setStyle('Fusion')
    
    window = WelcomeApp()
    window.show()
    sys.exit(app.exec())