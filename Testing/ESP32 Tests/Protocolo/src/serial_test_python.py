import serial

import serial
import serial.tools.list_ports
import time

SHORT_WAIT_TIME = 0.1
MEDIUM_WAIT_TIME = 2
LONG_WAIT_TIME = 3*60

class Serial:
	
    def __init__(self, port, baudrate) -> None:
        self.serial = serial.Serial(port=port, baudrate=baudrate, timeout=SHORT_WAIT_TIME)

    def read_serial_and_print(self, wait_time: float = SHORT_WAIT_TIME, print_description: str = ""):
        res = self.read_serial(wait_time)
        print(print_description, res)
        return res

    def write_serial(self, text):
        self.serial.write(text.encode())
        return
    
    def read_serial_until(self, last_line:bytes = b'OK\n', timeout:float = SHORT_WAIT_TIME, first_timeout:float = -1):
        data = []
        if first_timeout == -1:
            first_timeout = timeout
        self.serial.timeout = first_timeout
        data.append(self.serial.readline())
        self.serial.timeout = timeout
        while data[-1] != last_line and data[-1] != b'':
            data.append(self.serial.readline())
        return data

    def read_serial(self,timeout: float = SHORT_WAIT_TIME):
        self.serial.timeout = timeout
        data = self.serial.readline()
        return data.decode()      

port = Serial('COM3', 9600)
while(1):
    print(port.read_serial())