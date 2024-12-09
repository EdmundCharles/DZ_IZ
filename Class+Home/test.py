import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Открытие файла")
        
        self.button = QPushButton("Открыть файл", self)
        self.button.clicked.connect(self.open_file)
        self.button.setGeometry(10, 10, 150, 30)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 50, 400, 300)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Текстовые файлы (*.txt);;Все файлы (*)")
        if file_path:
            with open(file_path, 'r') as file:
                self.text_edit.setText(file.read())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
