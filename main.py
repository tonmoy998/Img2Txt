from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QTextEdit, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QFileDialog
from PySide6.QtCore import QSize, Qt
from pytesseract import Output, image_to_string, pytesseract
import pyperclip

import sys

from pytesseract.pytesseract import file_to_dict, main


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Img2Txt")

        self.label = QLabel("Enter path :")
        self.label.setStyleSheet(
            'font-size:30px;font-family:"ADlam Display", monospace;')

        self.select = QPushButton('')
        self.select.setStyleSheet("border-image : url('./img/select.png');")
        self.select.setFixedWidth(200)
        self.select.setFixedHeight(80)
        # self.select.setStyleSheet(
        # 'background-color:red;')

        self.copy = QPushButton("")
        self.copy.setFixedHeight(90)
        self.copy.setFixedWidth(220)
        self.copy.setStyleSheet('border-image:url("./img/copy.png");')
        self.copy.clicked.connect(self.copy_txt)
        # self.copy.clicked.connect()
        self.browse = QPushButton('')
        self.browse.setAutoFillBackground(True)
        self.browse.setStyleSheet("border-image : url('./img/browse.png');")
        # self.browse.setStyleSheet('background-color:green;')
        self.browse.setFixedHeight(80)
        self.browse.setFixedWidth(250)
        self.browse.clicked.connect(self.open_file)
        # self.copy.setFixedWidth(100)
        # self.copy.setFixedHeight(30)

        self.input = QLineEdit()
        self.output = QTextEdit()
        self.output.setFixedHeight(400)
        self.output.setStyleSheet(
            'font-size:18px;font-family:"Nerd Font",monospace;border:none;background-color:#fff;')

        self.input.setStyleSheet(
            'font-size:25px;border:none;background-color:#fff;')
        self.input.setFixedHeight(70)
        self.input.setFixedWidth(600)

        # btn acction
        self.select.clicked.connect(self.select_text)
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()

        h_layout.addWidget(self.label)
        h_layout.addWidget(self.input)
        h_layout.addWidget(self.select)

        v_layout.addWidget(self.browse)
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.output)
        v_layout.addWidget(self.copy)
        v_layout.setAlignment(self.browse, Qt.AlignmentFlag.AlignCenter)
        v_layout.setAlignment(self.copy, Qt.AlignmentFlag.AlignCenter)

        self.setLayout(v_layout)

    def select_text(self):
        path = self.input.text()
        text = pytesseract.image_to_string(path)
        self.output.setText(text)

    def open_file(self):
        file_brow = QFileDialog.getOpenFileName(
            self, 'Open file', '/home/tonmoy/Pictures/', "Images (*.png *.jpeg *.jpg)")
        file_path = file_brow[0]
        print(file_path)
        path = file_path
        self.input.setText(path)
        self.select_text()
        # file_path =

    def copy_txt(self):
        if (self.output.copy):
            self.copy.setStyleSheet('border-image:url("./img/copied.png");')
            self.output.copy()
        else:
            pass


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
