import json, os, datetime

with open(f'{os.path.dirname(__file__)}/database/data.json','r') as jsFile:
    metadata = json.load(jsFile)

PORT = metadata['SERVER']['PORT']
HEADER = metadata['SERVER']['HEADER']
FORMAT = metadata['SERVER']['FORMAT']
DISCONNECT = metadata['SERVER']['DISCONNECT']

class userClient:
    def send(client, msg:str):
        if msg:
            message = msg.encode(FORMAT)
            client.sendall(message)
            msg = client.recv(HEADER).decode(FORMAT)
            print(f'[{datetime.datetime.time(datetime.datetime.now())}] [SERVER] {msg}') 
            if message == DISCONNECT:
                print(f'[{datetime.datetime.time(datetime.datetime.now())}] [CLIENT] Closing client')
                client.close()

    def recieve(client, command:str):
        if command:
            client.sendall(command.encode(FORMAT))
            data = client.recv(HEADER).decode(FORMAT)
            return data