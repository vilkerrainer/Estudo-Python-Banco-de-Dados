from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calculadora")
        
        self.resize(800, 600)
        
        self.setMinimumSize(400, 300)
        self.setMaximumSize(1200, 800)
        
        self.label = QLabel("Clique no button")
        self.button = QPushButton("Clique-me")
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        
        self.button.clicked.connect(self.on_button_click)
        
    def on_button_click(self):
        self.label.setText("Olá, PyQt6!")

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()