import threading
import sys
import queue
import serial.serialutil
from serial import Serial
from serial.serialutil import SerialException
from serial.tools import list_ports

BAUD_RATE = 961_200
SERIAL_RECOGNIZER = "USB to UART Bridge"
biosc_queue = queue.Queue()
stdin_queue = queue.Queue()


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

        # Blink to indicate connection
        self.write(Commands.BLINK)
        self.write(Commands.LOW)

    @staticmethod
    def find_port():
        ports = list(list_ports.comports())
        try:
            esp32_port = [p for p in ports if SERIAL_RECOGNIZER in p.description][0].device
            return esp32_port
        except IndexError:
            print('No ESP32 found')
            return None

    def write(self, command: str, *args: str):
        if args:
            command = f"{command}-{'-'.join(args)}"
        self.serial_con.write(f"<{command}>".encode())
        # self.serial_con.readline() # Clear buffer

    def _readline(self):
        try:
            return self.serial_con.readline().decode()
        except SerialException:
            return ''

    def close(self):
        self.serial_con.close()

    def read_message(self):
        message = self._readline()
        if not message:
            print(message)
            return None, None
        try:
            msg_strings = message.split('-')
            command = msg_strings[0]
            data = msg_strings[1]
            self.command = command
            self.data = data
            return command, data
        except (IndexError, ValueError, TypeError):
            self.data = None
            return None, None


def get_biosc_msg(serial_con: BioscSerial):
    """
    This function is meant to be used in a separate thread to read the messages from the serial connection,
    and add them to the queue
    :param serial_con:
    """
    global biosc_queue
    while True:
        command, data = serial_con.read_message()
        if command is None:
            continue
        biosc_queue.put((command, data))


def get_stdin():
    """
    This function is meant to be used in a separate thread to read the messages from the GUI / console and forward them to the serial connection
    """
    global stdin_queue
    while True:
        try:
            command, *args = sys.stdin.readline().strip().split()
            stdin_queue.put((command, args))
            if command == Commands.EXIT:
                break
        except (EOFError, ValueError):
            continue


def handle_new_commands(serial_con: BioscSerial):
    """
    Handle the new commands from the queues
    :param serial_con: BioscSerial object
    """
    global biosc_queue
    global stdin_queue

    while True:
        # Handle input coming from the GUI / console
        if not stdin_queue.empty():
            command, args = stdin_queue.get()
            serial_con.write(command, *args)
            if command == Commands.EXIT:
                break

        # Handle input coming from the serial connection
        if not biosc_queue.empty():
            command, data = biosc_queue.get()
            if command == Commands.MEASURED_SIGNALS:
                sys.stdout.write(f"{command}-{data}\n")
                sys.stdout.flush()
            elif command == Commands.ERROR:
                sys.stderr.write(f"{command}-{data}\n")
                sys.stderr.flush()
            elif command == Commands.EXIT:
                break


def main():
    serial_con = BioscSerial()
    if serial_con.serial_con is None:
        sys.exit(1)

    print(f"Connected to {serial_con.port}")

    # Start the threads
    biosc_thread = threading.Thread(target=get_biosc_msg, args=(serial_con,))
    stdin_thread = threading.Thread(target=get_stdin)
    biosc_thread.start()
    stdin_thread.start()

    # Actual main functionality
    handle_new_commands(serial_con)

    # Close the serial connection on exit
    serial_con.write(Commands.STOP)
    serial_con.close()


if __name__ == '__main__':
    main()
