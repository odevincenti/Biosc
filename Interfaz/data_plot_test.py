import sys
import numpy as np
from PyQt6 import QtWidgets, QtCore, QtSerialPort
from PyQt6.QtGui import QWheelEvent
import pyqtgraph as pg

BAUD_RATE = 115200
DATA_LEN = 1000
BUFFER_SIZE = 100
REFRESH_RATE = 10  # Refresh rate in milliseconds


class SignalPlotter(pg.PlotWidget):
    def __init__(self):
        super().__init__()
        self.setRange(xRange=(0, DATA_LEN), disableAutoRange=True)

    def wheelEvent(self, event: QWheelEvent):
        # Get the current x and y ranges
        current_range = self.getViewBox().viewRange()
        old_range = current_range[0]

        # Zoom in or out
        delta = event.angleDelta().y()
        factor = 1.1 if delta > 0 else 0.9
        new_right_limit = old_range[1] * factor
        new_x_range = (0, new_right_limit)
        self.setRange(xRange=new_x_range)
        event.accept()


class Oscilloscope(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Digital Oscilloscope')

        # Set up the plot
        self.plot_widget = SignalPlotter()
        self.setCentralWidget(self.plot_widget)
        self.plot = self.plot_widget.plot(pen='r')

        # Set up a timer to refresh the plot
        self.timer = QtCore.QTimer()
        self.timer.setInterval(REFRESH_RATE)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        # Set up the serial port connection
        self.serial = QtSerialPort.QSerialPort()
        self.serial.setBaudRate(BAUD_RATE)
        self.serial.readyRead.connect(self.read_data)
        self.setup_serial()
        self.data = [0 for _ in range(DATA_LEN)]
        self.data_len = DATA_LEN

    def setup_serial(self):
        available_ports = QtSerialPort.QSerialPortInfo.availablePorts()
        for port in available_ports:
            if 'USB' in port.description():
                self.serial.setPort(port)
                if not self.serial.isOpen():
                    if not self.serial.open(QtCore.QIODeviceBase.OpenModeFlag.ReadWrite):
                        QtWidgets.QMessageBox.critical(self, 'Serial Port Error', f"Can't open {port.portName()}")
                    else:
                        print(f"Connected to {port.portName()}")
                break
        else:
            QtWidgets.QMessageBox.critical(self, 'Serial Port Error', 'No suitable serial port found.')
        self.serial.write(b's')

    def get_x_range(self):
        vb = self.plot_widget.getPlotItem().getViewBox()
        x_range = vb.viewRange()[0]  # First element is the x-axis range
        return x_range

    def read_data(self):
        if self.serial.isWritable():
            self.serial.write(b's')

        if self.serial.canReadLine():
            data = self.serial.read(BUFFER_SIZE)
            self.data.extend(data)
            x_range = self.get_x_range()
            self.data_len = int(x_range[1] - x_range[0]) + 1
            if len(self.data) > self.data_len:
                self.data = self.data[-self.data_len:]

    def update_plot(self):
        self.plot.setData(self.data)


def main():
    app = QtWidgets.QApplication(sys.argv)
    oscilloscope = Oscilloscope()
    oscilloscope.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
