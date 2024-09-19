import sys
from PySide6.QtWidgets import QApplication
import pyqtgraph as pg

uiclass, baseclass = pg.Qt.loadUiType("template.ui")

class MainWindow(uiclass, baseclass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()