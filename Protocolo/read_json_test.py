import json

def main():
    path = 'test_msg.json'
    with open(path, 'r') as f:
        message = f.read()
        print(message.split('\n'))
        data = message.split('\n')[1]
        data = json.loads(data)
    
    print(data, '\n')
    print(data[0], '\n')
    print(data[1], '\n')
    print(data[0]['channel'], '\n')
    print(data[0]['signal'], '\n')

if __name__ == '__main__':
    main()