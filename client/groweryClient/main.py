import socket, json, os, time

with open(f'{os.path.dirname(__file__)}/database/data.json','r') as jsFile:
    metadata = json.load(jsFile)

SERVER = socket.gethostbyname('192.168.1.22')
PORT = metadata['SERVER']['PORT']
HEADER = metadata['SERVER']['HEADER']
FORMAT = metadata['SERVER']['FORMAT']
DISCONNECT = metadata['SERVER']['DISCONNECT']
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

connected = False
while not connected:
    try:
        connected = True
    except socket.error as e:
        print(f'{e}')
        print('Connection to server failed, retrying...')
        time.sleep(10)
    finally:
        client.close()

class userClient:
    def __init__(self):
        self.send('groweryClient')
        
        while connected:
            self.send(input('[CLIENT] '))

    def send(self, msg):
        if msg:
            message = msg.encode(FORMAT)
            client.sendall(message)
            msg = client.recv(HEADER).decode(FORMAT)
            print(f'[SERVER] {msg}')
            if message == DISCONNECT:
                print('[CLIENT] Closing client.')
                self.connceted = False
                client.close()

if __name__ == '__main__':
    client = userClient()