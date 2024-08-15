import sys
from PyQt6 import QtWidgets, QtCore, QtSerialPort

class TestSerial(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.serial = QtSerialPort.QSerialPort()
        self.serial.setBaudRate(115200)
        self.serial.readyRead.connect(self.read_data)

        self.setup_serial()

    def setup_serial(self):
        available_ports = QtSerialPort.QSerialPortInfo.availablePorts()
        for port in available_ports:
            if 'USB' in port.description():
                self.serial.setPort(port)
                if self.serial.open(QtCore.QIODeviceBase.OpenModeFlag.ReadWrite):
                    print(f"Connected to {port.portName()}")
                    print("Serial port successfully opened.")
                else:
                    print("Failed to open serial port.")
                break

    def read_data(self):
        print('read data called')
        print("Reading data...")
        if self.serial.canReadLine():
            data = self.serial.readLine().data().decode().strip()
            print(f"Received data: {data}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    test_serial = TestSerial()
    test_serial.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
