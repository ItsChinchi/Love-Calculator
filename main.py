import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class LoveCalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.name1_label = QLabel("Enter your name:")
        self.name1_entry = QLineEdit()
        self.name2_label = QLabel("Enter your partner's name:")
        self.name2_entry = QLineEdit()

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_love)

        layout.addWidget(self.name1_label)
        layout.addWidget(self.name1_entry)
        layout.addWidget(self.name2_label)
        layout.addWidget(self.name2_entry)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)
        self.setWindowTitle("Love Calculator")

    def calculate_love(self):
        name1 = self.name1_entry.text()
        name2 = self.name2_entry.text()

        # Calculate a random compatibility score (for demonstration purposes)
        compatibility_score = random.randint(0, 100)

        result = f"{name1} and {name2}'s love compatibility is {compatibility_score}%!"
        QMessageBox.information(self, "Love Calculator Result", result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    love_calculator = LoveCalculatorApp()
    love_calculator.show()
    sys.exit(app.exec_())
