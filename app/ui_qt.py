from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QFormLayout, QMessageBox
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from app.calculator import calc_final
import sys


class OFPPTCalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OFPPT Grade Calculator")
        self.setFixedSize(400, 500)
        self.init_ui()

    def init_ui(self):
        font_label = QFont("Segoe UI", 10)
        font_input = QFont("Segoe UI", 10)
        font_result = QFont("Segoe UI", 11, QFont.Bold)

        form_layout = QFormLayout()
        self.inputs = {}

        fields = [
            "Note Passage", "Moyenne Modules", "Moyenne Théorie",
            "Moyenne Pratique", "Français", "Arabe", "Anglais"
        ]

        for field in fields:
            input_field = QLineEdit()
            input_field.setPlaceholderText("Ex: 14.5")
            input_field.setFont(font_input)
            self.inputs[field] = input_field
            form_layout.addRow(QLabel(field), input_field)

        self.result_label = QLabel("")
        self.result_label.setFont(font_result)
        self.result_label.setAlignment(Qt.AlignCenter)

        calc_button = QPushButton("Calculer")
        calc_button.setFont(QFont("Segoe UI", 10, QFont.Bold))
        calc_button.clicked.connect(self.calculate)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(calc_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate(self):
        try:
            values = [float(self.inputs[field].text()) for field in self.inputs]
            result = calc_final(*values)
            self.result_label.setText(f"Moyenne Générale : {result:.2f} / 20")
        except ValueError:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer toutes les notes correctement.")
            self.result_label.setText("")


def launch_app():
    app = QApplication(sys.argv)
    window = OFPPTCalculatorApp()
    window.show()
    sys.exit(app.exec())
