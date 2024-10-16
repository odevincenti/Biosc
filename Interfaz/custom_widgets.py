# The code is a simple digital oscilloscope that reads data from a serial port and plots it in real-time.

import sys
from PySide6 import QtWidgets, QtCore, QtSerialPort
import pyqtgraph as pg

BAUD_RATE = 115200
DATA_LEN = 4000
BUFFER_SIZE = 100
REFRESH_RATE = 10  # Refresh rate in milliseconds

class SerialReader(QtCore.QObject):
    data_received = QtCore.Signal(bytes)

    def __init__(self, serial_port):
        super().__init__()
        self.serial = serial_port

    @QtCore.Slot()
    def read_data(self):
        if self.serial.canReadLine():
            data = self.serial.read(BUFFER_SIZE)
            if data:
                self.data_received.emit(data)


class CustomScaleSpinBox(QtWidgets.QSpinBox):
    def __init__(self, parent=None):
        super(CustomScaleSpinBox, self).__init__(parent)
        self.units = [1, 2, 5, 10]
        self.scales = [1, 10, 100, 1000]
        self.current_scale_index = 0
        self.valid_values = self.get_valid_values()

        self.setRange(1, 10000)
        self.setSingleStep(1)

    def get_valid_values(self):
        # Generate the possible values based on units and scales
        valid_values = [unit * scale for scale in self.scales for unit in self.units]
        return sorted(set(valid_values))

    def stepBy(self, steps):
        current_value = self.value()

        # Find the nearest valid step
        if current_value in self.valid_values:
            current_index = self.valid_values.index(current_value)
        else:
            current_index = min(range(len(self.valid_values)), key=lambda i: abs(self.valid_values[i] - current_value))

        # Compute new index within valid ranges
        new_index = current_index + steps
        new_index = max(0, min(new_index, len(self.valid_values) - 1))

        # Set new value
        self.setValue(self.valid_values[new_index])

    def textFromValue(self, value):
        # Customize text display for "mV/div" or "V/div"
        if value >= 1000:
            return f"{value // 1000} V/div"
        else:
            return f"{value} mV/div"

    def valueFromText(self, text):
        # Extract numerical value from text
        text = text.replace(" V/div", "").replace(" mV/div", "")
        return float(text)


class SignalPlotter(pg.PlotWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set y range to 10 divisions, from -5 to 5, and dynamic x range, no auto range
        self.setRange(yRange=(-5, 5), disableAutoRange=True)
        self.setRange(xRange=(0, DATA_LEN), disableAutoRange=True, padding=0)

        # Disable dragging
        self.setMouseEnabled(x=False, y=False)

        # Set up the grid
        self.showGrid(x=True, y=True)

        # Add a draggable horizontal, cyan, dashed, draggable line. Set cursor to open hand, close hand when hovering
        self.trigger_pen = pg.mkPen(color='cyan', style=QtCore.Qt.DashLine, width=2)
        self.triggerLine = pg.InfiniteLine(movable=True, angle=0, pen=self.trigger_pen)
        self.triggerLine.setCursor(QtCore.Qt.OpenHandCursor)
        self.triggerLine.setHoverPen(pg.mkPen(color='cyan', style=QtCore.Qt.DashLine, width=3))

        # Add the line to the plot, above all other plot lines, and lock it at the top layer
        self.addItem(self.triggerLine)
        self.triggerLine.setZValue(10)

        # Change cursor to closed hand when the line is being moved
        self.triggerLine.sigDragged.connect(lambda: self.triggerLine.setCursor(QtCore.Qt.ClosedHandCursor))
        self.triggerLine.sigPositionChangeFinished.connect(lambda: self.triggerLine.setCursor(QtCore.Qt.OpenHandCursor))

    def wheelEvent(self, event):
        current_range = self.getViewBox().viewRange()
        old_range = current_range[0]

        # Zoom in or out
        delta = event.angleDelta().y()
        factor = 1.1 if delta > 0 else 0.9
        new_right_limit = old_range[1] * factor
        new_x_range = (0, new_right_limit)
        if new_right_limit < DATA_LEN:
            self.setRange(xRange=new_x_range, padding=0)
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
