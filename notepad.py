import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QTabWidget, QColorDialog
from PyQt5.QtGui import QFont

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("Archivo")

        new_tab_action = QAction("Nueva Pestaña", self)
        new_tab_action.triggered.connect(self.new_tab)
        file_menu.addAction(new_tab_action)

        open_action = QAction("Abrir", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("Guardar", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        close_tab_action = QAction("Cerrar Pestaña", self)
        close_tab_action.triggered.connect(self.close_tab)
        file_menu.addAction(close_tab_action)

        self.new_tab()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Bloc de Notas')
        self.show()

    def new_tab(self):
        text_edit = QTextEdit()
        font = QFont("Arial", 12)
        text_edit.setFont(font)
        self.tabs.addTab(text_edit, "Nueva Pestaña")

def main():
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
