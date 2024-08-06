import sys
import serial
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import pyqtgraph as pg

BAUD_RATE = 115200

class Oscilloscope(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.serial = QSerialPort()
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
        self.timer.setInterval(50)  # Refresh rate in milliseconds
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        # Set up the serial port connection
        self.setup_serial()

    def setup_serial(self):
        available_ports = QSerialPortInfo.availablePorts()
        for port in available_ports:
            if 'USB' in port.description():
                self.serial.setPort(port)
                if not self.serial.isOpen():
                    if not self.serial.open(QtCore.QIODevice.ReadOnly):
                        QtWidgets.QMessageBox.critical(self, 'Serial Port Error', f"Can't open {port.portName()}")
                    else:
                        print(f"Connected to {port.portName()}")
                break
        else:
            QtWidgets.QMessageBox.critical(self, 'Serial Port Error', 'No suitable serial port found.')

    def read_data(self):
        if self.serial.canReadLine():
            try:
                data = self.serial.readLine().data().decode().strip()
                self.data.append(float(data))
                if len(self.data) > 1000:  # Limit the data length for performance
                    self.data = self.data[-1000:]
            except ValueError:
                pass

    def update_plot(self):
        self.plot.setData(self.data)

def main():
    app = QtWidgets.QApplication(sys.argv)
    oscilloscope = Oscilloscope()
    oscilloscope.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
