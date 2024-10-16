import sys
from PySide6.QtWidgets import QApplication
from PySide6 import QtCore
import pyqtgraph as pg
import numpy as np

uiclass, baseclass = pg.Qt.loadUiType("template.ui")

class MainWindow(uiclass, baseclass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.widget.plot(np.sin(2*np.pi*0.01*np.arange(10000)) + 0.05*np.random.normal(size=10000), pen=(255,0,0))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()