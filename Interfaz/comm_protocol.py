import threading
import sys

import serial.serialutil
from serial import Serial
from serial.tools import list_ports

BAUD_RATE = 9600
SERIAL_RECOGNIZER = "USB to UART Bridge"


class Commands:
    RUN = 'R'
    STOP = 'S'
    SINGLE = 'S1'
    HIGH = 'H'
    LOW = 'L'
    BLINK = 'B'
    MEASURED_SIGNALS = 'MS'
    ACTIVATE_CHANNEL = 'AC'
    DEACTIVATE_CHANNEL = 'DC'
    MEASURE_WAVEGEN = 'MW'
    STOP_MEASURE_WAVEGEN = 'SW'
    ERROR = 'ER'
    EXIT = 'exit'

    def __iter__(self):
        yield Commands.RUN
        yield Commands.STOP
        yield Commands.SINGLE
        yield Commands.HIGH
        yield Commands.LOW
        yield Commands.BLINK
        yield Commands.MEASURED_SIGNALS
        yield Commands.ACTIVATE_CHANNEL
        yield Commands.DEACTIVATE_CHANNEL
        yield Commands.MEASURE_WAVEGEN
        yield Commands.STOP_MEASURE_WAVEGEN
        yield Commands.ERROR
        yield Commands.EXIT


class BioscSerial:
    def __init__(self, baud_rate=BAUD_RATE):
        self.command = None
        self.data = None
        self.baud_rate = baud_rate
        self.port = self.find_port()
        try:
            self.serial_con = Serial(self.port, self.baud_rate)
        except serial.serialutil.SerialException:
            self.serial_con = None

    @staticmethod
    def find_port():
        ports = list(list_ports.comports())
        try:
            esp32_port = [p for p in ports if SERIAL_RECOGNIZER in p.description][0].device
            return esp32_port
        except IndexError:
            print('No ESP32 found')
            return None

    def write(self, command):
        self.serial_con.write(f"<{command}>".encode())
        self.serial_con.readline() # Clear buffer

    def _readline(self):
        return self.serial_con.readline().decode()

    def close(self):
        self.serial_con.close()

    def read_message(self, verbose=False):
        message = self._readline()
        # msg_strings = message.split('-')
        # command = msg_strings[0]
        # data = msg_strings[1]
        #
        # self.command = command
        # self.data = data


def stream_serial_data(serial_con: BioscSerial) -> bool:
    """
    Read a single message from the ESP through serial
    :param serial_con:
    :return:
    """
    serial_con.read_message()
    if serial_con.data is None:
        return False
    sys.stdout.write(serial_con.data)
    sys.stdout.flush()
    return True


def manage_input(serial_con: BioscSerial):
    """
    Read input data and preprocess the message
    """
    global running
    global command
    global args
    try:
        control = sys.stdin.readline().strip('\n').split('-')
        command, *args = control
        if command not in list(Commands()):
            raise ValueError(f"Invalid command")
        elif command in [Commands.STOP, Commands.EXIT]:
            running = False
        serial_con.write(command)

    except ValueError as e:
        print(e)
        sys.stderr.write('3')
        sys.stderr.flush()
    except KeyboardInterrupt:
        running = False
        command = Commands.EXIT


def main():
    """
    Main function to run the serial communication with the ESP32
    Translates the commands from the GUI to the ESP32
    If running this script directly, the commands should be entered manually (for testing purposes)
    :return:
    """
    global running
    global command
    global args

    biosc_serial = BioscSerial()
    if biosc_serial.serial_con is None:
        sys.exit(1)
    else:
        print('Serial connection established')

    running = True
    while running:
        pass

if __name__ == '__main__':
    command = None
    running = False
    args = None
    main()
