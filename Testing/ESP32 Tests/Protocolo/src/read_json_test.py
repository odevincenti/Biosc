import json
from serial import Serial
from serial.tools import list_ports
import matplotlib.pyplot as plt

BAUD_RATE = 9600

def process_message(message):
    print(message.split('-'))
    data = message.split('-')[1]
    data = json.loads(data)
    ch1 = data[0]

    plt.plot(ch1['signal'])
    plt.show()  


def main():
    ports = list(list_ports.comports())
    try:
        esp32_port = [p for p in ports if 'USB' in p.description][0].device
    except IndexError:
        print('No ESP32 found')
        return
    
    serial_con = Serial(esp32_port, BAUD_RATE)
    print('Serial connection established')
    
    command = '<H>'
    while command != '<exit>':
        command = input('Enter command: ')
        if '<' not in command or '>' not in command:
            print('Invalid command')
            continue
        serial_con.write(command.upper().encode())
        serial_con.readline()
        if command == '<MS>':
            message = serial_con.readline().decode().strip()
            print('Message:', message)
            if 'MS-' in message:
                process_message(message)
    

if __name__ == '__main__':
    main()


