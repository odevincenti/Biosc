import sys
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWidgets import QApplication
from PySide6 import QtCore
import pyqtgraph as pg
import numpy as np
from template_ui import Ui_Bioscope

TEST_SIG_LEN = 2_000_000

class MainWindow(QMainWindow, Ui_Bioscope):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Bioscope')

        # Dummy signals for testing
        self.dummy_signal = 100*np.sin(2*np.pi*1e-4*np.arange(TEST_SIG_LEN)) + 5*np.random.normal(size=TEST_SIG_LEN)
        self.update_plot()

        # Connect the spinbox to the plot
        self.spinScaleCH1.valueChanged.connect(self.update_plot)

        # Connect the trigger button to the trigger line method from the plot widget
        self.setup_capture_combo()
        self.comboMode.currentTextChanged.connect(self.setup_capture_combo)
        self.comboMode.setCurrentText('Trigger')

    def update_plot(self):
        scale = self.spinScaleCH1.value()
        self.plotWidget.clear()
        self.plotWidget.plot(self.dummy_signal/scale, pen=(255,0,0))

    def setup_capture_combo(self):
        capture_mode = self.comboMode.currentText()
        if capture_mode == 'Trigger':
            self.setup_capture_trigger()
        else:
            # Disable all trigger related widgets, and trigger line
            self.plotWidget.remove_trigger_line()
            self.comboTriggerCH.setEnabled(False)
            self.comboTriggerSet.setEnabled(False)

            if capture_mode == 'Roll':
                self.setup_capture_roll()
            elif capture_mode == 'XY':
                self.setup_capture_xy()


    def setup_capture_trigger(self):
        # Enable the trigger line
        self.plotWidget.set_trigger_line()

        # Enable the trigger channel and trigger set widgets
        self.comboTriggerCH.setEnabled(True)
        self.comboTriggerSet.setEnabled(True)

    def setup_capture_roll(self):
        print('roll selected')

    def setup_capture_xy(self):
        print('xy selected')


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()