from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QLabel
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QApplication
import sys

BAUD_RATE = 961_200
SERIAL_RECOGNIZER = "USB to UART Bridge"


class ESPSerial(QObject):
    data_received = Signal(str)
    error_occurred = Signal(str)

    def __init__(self, baud_rate=BAUD_RATE, parent=None):
        super().__init__(parent)
        self.serial_port = QSerialPort()
        self.serial_port.setBaudRate(baud_rate)
        self.serial_port.readyRead.connect(self.read_data)  # Connect readyRead signal

        self.port_name = self.find_port()

        if self.port_name:
            self.serial_port.setPortName(self.port_name)
            if not self.serial_port.open(QSerialPort.ReadWrite):
                self.error_occurred.emit(f"Failed to open port {self.port_name}.")
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

    def write_data(self, command: str):
        """Send data to the ESP32."""
        if self.serial_port.isOpen():
            self.serial_port.write(f"<{command}>\n".encode("utf-8"))
            self.serial_port.flush()
        else:
            self.error_occurred.emit("Serial port is not open.")

    def close(self):
        """Close the serial port."""
        self.serial_port.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ESP Communication")

        # Set up the main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Line edit for command input
        self.command_input = QLineEdit(self)
        self.command_input.setPlaceholderText("Enter command")
        self.layout.addWidget(self.command_input)

        # Button to send command
        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.send_command)
        self.layout.addWidget(self.send_button)

        # Text edit to display received data
        self.data_log = QTextEdit(self)
        self.data_log.setReadOnly(True)  # Prevent user editing
        self.layout.addWidget(self.data_log)

        # Status label
        self.status_label = QLabel("Status: Ready", self)
        self.layout.addWidget(self.status_label)

        # Initialize ESPSerial object
        self.esp_serial = ESPSerial()
        self.esp_serial.data_received.connect(self.append_to_log)
        self.esp_serial.error_occurred.connect(self.show_error)

    @Slot()
    def send_command(self):
        command = self.command_input.text().strip()
        if command:
            self.esp_serial.write_data(command)
            self.command_input.clear()

    @Slot(str)
    def append_to_log(self, data):
        """Append received data to the log."""
        self.data_log.append(f"> {data}")

    @Slot(str)
    def show_error(self, error):
        """Display errors in the status label."""
        self.status_label.setText(f"Status: {error}")

    def closeEvent(self, event):
        """Handle window close event."""
        self.esp_serial.close()
        event.accept()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()