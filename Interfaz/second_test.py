import sys
import threading
import serial
import time
from collections import deque
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg

class SerialReader(threading.Thread):
    def __init__(self, port, baud_rate, buffer_size=100):
        super().__init__()
        self.serial_port = serial.Serial(port, baud_rate)
        self.buffer_size = buffer_size
        self.data_buffer = deque(maxlen=buffer_size)
        self.new_data_event = threading.Event()
        self.running = True

    def run(self):
        while self.running:
            if self.serial_port.in_waiting > 0:
                command = self.serial_port.read().decode('utf-8')
                if command == 's':
                    data = []
                    for _ in range(self.buffer_size):
                        high = self.serial_port.read()
                        low = self.serial_port.read()
                        value = (ord(high) << 8) | ord(low)
                        data.append(value)
                    self.data_buffer.extend(data)
                    self.new_data_event.set()

    def stop(self):
        self.running = False
        self.serial_port.close()

class PlotterApp(QtWidgets.QMainWindow):
    def __init__(self, port='COM3', baud_rate=115200):
        super().__init__()
        self.initUI()
        self.serial_reader = SerialReader(port, baud_rate)
        self.serial_reader.start()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(50)

    def initUI(self):
        self.setWindowTitle('Real-Time Serial Plotter')
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.setYRange(0, 1023)
        self.data_line = self.graphWidget.plot()
        self.show()

    def update_plot(self):
        if self.serial_reader.new_data_event.is_set():
            data = list(self.serial_reader.data_buffer)
            self.data_line.setData(data)
            self.serial_reader.new_data_event.clear()

    def closeEvent(self, event):
        self.serial_reader.stop()
        self.serial_reader.join()
        event.accept()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = PlotterApp(port='COM9', baud_rate=115200)
    sys.exit(app.exec_())
