import json
from serial import Serial
from serial.tools import list_ports

BAUD_RATE = 9600

def process_message(message):
    print(message.split('-'))
    data = message.split('-')[1]
    data = json.loads(data)
    
    print(data, '\n')
    print(data[0], '\n')
    print(data[1], '\n')
    print(data[0]['channel'], '\n')
    print(data[0]['signal'], '\n')


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
    while command != 'exit':
        command = input('Enter command: ')
        serial_con.write(command.encode())
        message = serial_con.readline().decode()
        print('Message:', message)
        if command == '<MS>':
            process_message(message)
    

if __name__ == '__main__':
    main()


