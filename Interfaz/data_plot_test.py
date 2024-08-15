import sys
import numpy as np
from PyQt6 import QtWidgets, QtCore, QtSerialPort
import pyqtgraph as pg

BAUD_RATE = 115200
DATA_LEN = 1000
BUFFER_SIZE = 100
REFRESH_RATE = 50 # Refresh rate in milliseconds

class Oscilloscope(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.serial = QtSerialPort.QSerialPort()
        self.serial.setBaudRate(BAUD_RATE)
        self.serial.readyRead.connect(self.read_data)

        self.init_ui()
        self.data = []

    def init_ui(self):
        self.setWindowTitle('Digital Oscilloscope')

        # Set up the plot
        self.plot_widget = pg.PlotWidget()
        self.setCentralWidget(self.plot_widget)
        self.plot = self.plot_widget.plot()

        # Set up a timer to refresh the plot
        self.timer = QtCore.QTimer()
        self.timer.setInterval(REFRESH_RATE)  
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        # Set up the serial port connection
        self.setup_serial()

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


    def read_data(self):
        if self.serial.isWritable():
            self.serial.write(b's')

        if self.serial.canReadLine():
            try:
                data = self.serial.read(BUFFER_SIZE)
                self.data.extend(data)
                if len(self.data) > DATA_LEN:
                    self.data = self.data[-DATA_LEN:]
            except ValueError:
                pass

    def update_plot(self):
        self.plot.setData(self.data)

def main():
    app = QtWidgets.QApplication(sys.argv)
    oscilloscope = Oscilloscope()
    oscilloscope.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
