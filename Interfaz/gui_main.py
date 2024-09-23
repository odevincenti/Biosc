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
        self.widget.plot(np.random.normal(size=1000), pen=(255,0,0))
        # Add a horizontal line at y=1 with dashed white pen
        self.widget.addLine(y=1, pen=pg.mkPen('w', width=1, style=QtCore.Qt.DashLine))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()