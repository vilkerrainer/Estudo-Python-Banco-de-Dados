from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setGeometry(100, 100, 300, 400)
        self.create_ui()
        
    def create_ui(self):
        # Layout principal
        main_layout = QVBoxLayout()
        
        # Caixa de entrada (display)
        self.display = QLineEdit()
        self.display.setReadOnly(True)  # Tornar o display não editável diretamente
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("font-size: 24px")
        main_layout.addWidget(self.display)
        
        # Layout para botões
        grid_layout = QGridLayout()
        
        # Lista de botões
        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), 'C': (3, 1), '=': (3, 2), '+': (3, 3),
        }
        
        # Criar botões e adicionar ao layout
        for text, pos in buttons.items():
            button = QPushButton(text)
            button.setFixedSize(60, 60)
            button.setStyleSheet("font-size: 18px")
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, pos[0], pos[1])
        
        # Adicionar o grid layout ao layout principal
        main_layout.addLayout(grid_layout)
        
        # Definir o layout principal
        self.setLayout(main_layout)
    
    def on_button_click(self):
        # Obtém o botão que foi clicado
        button = self.sender()
        text = button.text()

        if text == 'C':
            self.display.clear()  # Limpa o display
        elif text == '=':
            try:
                expression = self.display.text()
                result = eval(expression)  # Avalia a expressão
                self.display.setText(str(result))
            except:
                self.display.setText("Erro")
        else:
            # Adiciona o texto do botão ao display
            current_text = self.display.text()
            new_text = current_text + text
            self.display.setText(new_text)

def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
