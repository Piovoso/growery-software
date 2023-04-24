import tkinter as tk, json, socket, os, time
from clientFunc import userClient

with open(f'{os.path.dirname(__file__)}/database/data.json','r') as jsFile:
    metadata = json.load(jsFile)

VERSION = metadata['VERSION']
SERVER = socket.gethostbyname('192.168.1.22')
PORT = metadata['SERVER']['PORT']
ADDR = (SERVER, PORT)
DISCONNECT = metadata['SERVER']['DISCONNECT']

connected = False
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while not connected:
    try:
        client.connect(ADDR)
        connected = True
    except socket.error:
        print('Connection to server failed, retrying...')
        time.sleep(10)
        pass


class ClientLogin:
    def __init__(self):
        try: userClient.send(client ,'userClient')
        except (ConnectionError):
            print(f'{ConnectionError}')
        self.root = tk.Tk()
        self.root.geometry(f"{int(self.root.winfo_screenwidth()/6.4)}x{int(self.root.winfo_screenheight()/2.7)}")
        self.root.title(f"PyMonitor Client {VERSION}")
        self.root.resizable(0,0)

        ClientLogin.styling(self.root)
        ClientLogin.login(self.root)

        self.root.mainloop()

    def login(self):
        self.loginFrame = tk.Frame(self, background="#363636")
        self.loginFrame.place(relx=0, rely=0.75, relheight=0.25, relwidth=1)

        self.usernameLabel = tk.Label(self.loginFrame, text="Username:", background="#363636", foreground="#d9d9d9")
        self.usernameLabel.place(relx=0.05, rely=0.1, relheight=0.2, relwidth=0.225)
        usr = tk.StringVar(self)
        self.username = tk.Entry(self.loginFrame, textvariable = usr, background="#363636", foreground="#d9d9d9")
        self.username.place(relx=0.3, rely=0.1, relheight=0.2, relwidth=0.65)
        
        self.passwordLabel = tk.Label(self.loginFrame, text="Password:", background="#363636", foreground="#d9d9d9")
        self.passwordLabel.place(relx=0.05, rely=0.35, relheight=0.2, relwidth=0.225)
        psw = tk.StringVar(self)
        self.password = tk.Entry(self.loginFrame, textvariable = psw, show="*", background="#363636", foreground="#d9d9d9")
        self.password.place(relx=0.3, rely=0.35, relheight=0.2, relwidth=0.65)

        self.loginButton = tk.Button(self.loginFrame, text="Login", background="#d60000",
                                     foreground="#d9d9d9", relief="flat",
                                     command=lambda: ClientLogin.forward(self, client, f'{usr.get()},{psw.get()}'))
        self.loginButton.place(relx=0.05, rely=0.65, relheight=0.3, relwidth=0.9)

    def styling(self):
        self.styleFrame = tk.Frame(self, background="#363636")
        self.styleFrame.place(relx=0, rely=0, relheight=0.75, relwidth=1)
        self.activeGrowery = tk.Label(self.styleFrame, text=f'Active Groweries: {userClient.recieve(client, "activeGrowery")}')
        self.activeGrowery.place(relx=0, rely=0, relheight=0.2, relwidth=1)
    
    def forward(self, client, message):
        userClient.send(client, message)
        self.destroy()
        ClientMonitor()

class ClientMonitor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{int(self.root.winfo_screenwidth()/1.5)}x{int(self.root.winfo_screenheight()/1.5)}")
        self.root.title(f"PyMonitor Client {VERSION}")
        self.root.resizable(0,0)

        ClientMonitor.notification(self.root)
        ClientMonitor.main(self.root)

        self.root.mainloop()

    def notification(self):
        self.notificationFrame = tk.Frame(self, background="#363636")
        self.notificationFrame.place(relx=0, rely=0, relheight=0.05, relwidth=1)

        self.alerts = tk.Button(self.notificationFrame, text="Alerts", background="#d60000", foreground="#d9d9d9", relief="groove")
        self.alerts.place(relx=0.002, rely=0.05, relheight=0.9, relwidth=0.1)

        self.newSeed = tk.Button(self.notificationFrame, text="New Seed", background="#666", foreground="#d9d9d9", relief="groove")
        self.newSeed.place(relx=0.5, rely=0.05, relheight=0.9, relwidth=0.075)

        self.exit =tk.Button(self.notificationFrame, text="Exit", background="#d60000", foreground="#d9d9d9", relief="groove", command=lambda: ClientMonitor.exit(self))
        self.exit.place(relx=0.949, rely=0.05, relheight=0.9, relwidth=0.05)

    def main(self):
        self.mainFrame = tk.Frame(self, background="#363636")
        self.mainFrame.place(relx=0, rely=0.05, relheight=0.95, relwidth=1)
        self.temporaryButton = tk.Button(self, text='Test', command=lambda: userClient.send(client, 'UngaBunga'))
        self.temporaryButton.place(relx=0.4, rely=0.4, relheight=0.2, relwidth=0.2)
    
    def exit(self):
        try:
            userClient.send(client, DISCONNECT)
        except (ConnectionAbortedError):
            print(f'ConnectionAbortedError: An established connection was aborted by the software in your host machine')
        
        self.destroy()


if __name__ == '__main__':
    client = ClientLogin()