import sys
from PySide6 import QtWidgets, QtCore, QtSerialPort
from Interfaz.custom_widgets import SignalPlotter, REFRESH_RATE, DATA_LEN, BAUD_RATE, SerialReader


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

        # Initialize data buffer
        self.data = [0 for _ in range(DATA_LEN)]
        self.data_len = DATA_LEN

        # Set up the serial port in the main thread
        port_name = self.get_serial_port()
        if port_name:
            self.serial = QtSerialPort.QSerialPort()
            self.serial.setPortName(port_name)
            self.serial.setBaudRate(BAUD_RATE)
            if not self.serial.open(QtCore.QIODeviceBase.ReadWrite):
                QtWidgets.QMessageBox.critical(self, 'Serial Port Error', f"Can't open {port_name}")
                self.close()
                return

            self.serial.write(b's')

            # Set up the serial reader in a separate thread
            self.serial_thread = QtCore.QThread()
            self.reader = SerialReader(self.serial)
            self.reader.moveToThread(self.serial_thread)
            self.reader.data_received.connect(self.process_serial_data)
            self.serial.readyRead.connect(self.reader.read_data)

            # Start the thread
            self.serial_thread.start()

        else:
            QtWidgets.QMessageBox.critical(self, 'Serial Port Error', 'No suitable serial port found.')
            self.close()

    @staticmethod
    def get_serial_port():
        available_ports = QtSerialPort.QSerialPortInfo.availablePorts()
        for port in available_ports:
            if 'USB' in port.description():
                return port.portName()
        return None

    def get_x_range(self):
        vb = self.plot_widget.getPlotItem().getViewBox()
        x_range = vb.viewRange()[0]  # First element is the x-axis range
        return x_range

    @QtCore.Slot(bytes)
    def process_serial_data(self, data):
        self.data.extend(data)
        x_range = self.get_x_range()
        # self.data_len = int(x_range[1] - x_range[0]) + 1
        if len(self.data) > self.data_len:
            self.data = self.data[-self.data_len:]

    def update_plot(self):
        self.serial.write(b's')
        self.plot.setData(self.data)

    def closeEvent(self, event):
        if hasattr(self, 'serial_thread') and self.serial_thread.isRunning():
            self.serial_thread.quit()
            self.serial_thread.wait()

        if self.serial.isOpen():
            self.serial.close()

        event.accept()


def main():
    app = QtWidgets.QApplication(sys.argv)
    oscilloscope = Oscilloscope()
    oscilloscope.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()