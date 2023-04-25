import socket, threading, json, os, datetime

class ClientHandle:
    def __init__(self):
        self.GroweryClientList = []
        self.UserClientList = []

        with open(f'{os.path.dirname(__file__)}/database/data.json','r') as jsFile:
            self.metadata = json.load(jsFile)

        self.SERVER = socket.gethostbyname('192.168.1.22')
        self.PORT = self.metadata['SERVER']['PORT']
        self.HEADER = self.metadata['SERVER']['HEADER']
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = self.metadata['SERVER']['FORMAT']
        self.DISCONNECT = self.metadata['SERVER']['DISCONNECT']

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(self.ADDR)
        server.listen()

        print(f'[{datetime.datetime.time(datetime.datetime.now())}] [SERVER] Listening on {self.SERVER}:{self.PORT}')
        while True:
            conn, addr = server.accept()
            clientType = conn.recv(self.HEADER).decode(self.FORMAT)

            if clientType == 'UserClient':
                self.UserClientList.append(addr)
                
                conn.sendall('User client selected... Please Log in'.encode(self.FORMAT))
                conn.sendall(str(len(self.GroweryClientList)).encode(self.FORMAT))
                userThread = threading.Thread(target=self.UserClient, args=(conn, addr))
                userThread.start()

            elif clientType == 'GroweryClient':
                self.GroweryClientList.append(addr)

                conn.sendall('Growery client selected... Please Log in'.encode(self.FORMAT))
                groweryThread = threading.Thread(target=self.GroweryClient, args=(conn, addr))
                groweryThread.start()
            
            else:
                conn.sendall('Incorrect client type'.encode(self.FORMAT))
                conn.close()

    def UserClient(self, user, addr):
        print(f'[{datetime.datetime.time(datetime.datetime.now())}] [NEW] {addr[0]}:{addr[1]} connected')

        self.Authentication(user)

        connected = True
        while connected:
            try:
                msg = user.recv(self.HEADER).decode(self.FORMAT)
                print(f'[{datetime.datetime.time(datetime.datetime.now())}] [{addr[0]}:{addr[1]}] {msg}')
                if msg == 'activeGrowery':
                    user.sendall(str(len(self.GroweryClientList)).encode(self.FORMAT))
                elif msg == self.DISCONNECT:
                    connected = False
                    user.close()
                else:
                    user.sendall('Recieved'.encode(self.FORMAT))
            except:
                connected = False
                print(f'[{datetime.datetime.time(datetime.datetime.now())}] [{addr[0]}:{addr[1]}] User exited unexpectedly')
                user.close()

    def GroweryClient(self, growery, addr):
        print(f'[{datetime.datetime.time(datetime.datetime.now())}] [NEW] {addr[0]}:{addr[1]} connected')

        self.Authentication(growery, 'GroweryClient')

        connected = True
        while connected:
            try:
                msg = growery.recv(self.HEADER).decode(self.FORMAT)

                print(f'[{addr[0]}:{addr[1]}] {msg}')
                growery.sendall('Recieved'.encode(self.FORMAT))

                if msg == self.DISCONNECT:
                    connected = False
                    growery.close()
            except:
                connected = False
                print(f'[{datetime.datetime.time(datetime.datetime.now())}] [{addr[0]}:{addr[1]}] Growery exited unexpectedly')
                growery.close()


    def Authentication(self, client, clientType:str = 'UserClient'):

        USERNAME = self.metadata['CLIENT'][clientType]['USERNAME']
        PASSWORD = self.metadata['CLIENT'][clientType]['PASSWORD']

        authenticated = False
        while not authenticated:
            # Receive the username and password from the client
            try: data = client.recv(self.HEADER).decode(self.FORMAT)
            except: break
            try:
                client_username, client_password = data.split(",")
            
                # Check if the username and password are correct
                if client_username == USERNAME and client_password == PASSWORD:
                    authenticated = True
                    message = "Authentication successful"
                    print(f'[{datetime.datetime.time(datetime.datetime.now())}] [CLIENT] {message}')
                    # Send a confirmation message to the client
                    client.sendall(message.encode(self.FORMAT))
                else:
                    message = "Authentication failed"
                    print(f'[{datetime.datetime.time(datetime.datetime.now())}] [CLIENT] {message}')
                    # Send an error message to the client
                    client.sendall(message.encode(self.FORMAT))
                    # Close the connection and wait for a new connection
                    client.close()
                    break
            except:
                client.sendall('Incorrect login format, arguments must be seperated by coma'.encode(self.FORMAT))

if __name__ == '__main__':
    print(f'[{datetime.datetime.time(datetime.datetime.now())}] [SERVER] initializing...')
    server = ClientHandle()