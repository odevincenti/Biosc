from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QObject, Signal, Slot, QThread, QCoreApplication
from comm_protocol import Commands
import sys

BAUD_RATE = 961_200
SERIAL_RECOGNIZER = "USB to UART Bridge"  # Adjust this to match your ESP32's description

class ESPSerial(QObject):
    data_received = Signal(str)  # Signal emitted when new data is received
    error_occurred = Signal(str)  # Signal emitted for errors

    def __init__(self, baud_rate=115200, parent=None):
        super().__init__(parent)
        self.serial_port = QSerialPort()
        self.serial_port.setBaudRate(baud_rate)
        self.serial_port.readyRead.connect(self.read_data)  # Connect readyRead signal

        self.port_name = self.find_port()

        if self.port_name:
            self.serial_port.setPortName(self.port_name)
            if not self.serial_port.open(QSerialPort.ReadWrite):
                self.error_occurred.emit(f"Failed to open port {self.port_name}.")
            # Quick blink to indicate connection
            self.write_data(Commands.BLINK)
            self.write_data(Commands.LOW)
        else:
            self.error_occurred.emit("No ESP32 device found. Check connections!")

    @staticmethod
    def find_port():
        """Find the serial port corresponding to the ESP32."""
        for port in QSerialPortInfo.availablePorts():
            if SERIAL_RECOGNIZER in port.description():
                return port.portName()
        return None

    @Slot()
    def read_data(self):
        """Read data asynchronously when available."""
        while self.serial_port.canReadLine():
            data = self.serial_port.readLine().data().decode("utf-8").strip()
            self.data_received.emit(data)

    def write_data(self, command: str, *args):
        """Send data to the ESP32."""
        if args:
            command = f"{command}-{'-'.join(args)}"
        if self.serial_port.isOpen():
            self.serial_port.write(f"<{command}>\n".encode("utf-8"))
            self.serial_port.flush()
        else:
            self.error_occurred.emit("Serial port is not open.")


if __name__ == "__main__":
    pass
