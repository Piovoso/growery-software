import tkinter as tk
import json as js



class ClientLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{int(self.root.winfo_screenwidth()/6.4)}x{int(self.root.winfo_screenheight()/2.7)}")
        self.root.title("PyMonitor Client 0.1")
        self.root.resizable(0,0)

        ClientLogin.styling(self.root)

        ClientLogin.login(self.root)

        self.root.mainloop()

    def login(self):
        self.loginFrame = tk.Frame(self, background="#363636")
        self.loginFrame.place(relx=0, rely=0.75, height=100, width=300)

        self.usernameLabel = tk.Label(self.loginFrame, text="Username:", background="#363636", foreground="#d9d9d9")
        self.usernameLabel.place(relx=0.05, rely=0.1, relheight=0.2, relwidth=0.225)
        self.username = tk.Entry(self.loginFrame, text="Username", background="#363636", foreground="#d9d9d9")
        self.username.place(relx=0.3, rely=0.1, relheight=0.2, relwidth=0.65)
        
        self.passwordLabel = tk.Label(self.loginFrame, text="Password:", background="#363636", foreground="#d9d9d9")
        self.passwordLabel.place(relx=0.05, rely=0.35, relheight=0.2, relwidth=0.225)
        self.password = tk.Entry(self.loginFrame, show="*", text="Password", background="#363636", foreground="#d9d9d9")
        self.password.place(relx=0.3, rely=0.35, relheight=0.2, relwidth=0.65)

        self.loginButton = tk.Button(self.loginFrame, text="Login", background="#d60000",
                                     foreground="#d9d9d9", relief="flat", borderwidth=1, borderradius= 0,
                                     command=lambda a = self: ClientLogin.successful(a))
        self.loginButton.place(relx=0.05, rely=0.65, relheight=0.3, relwidth=0.9)

    def styling(self):
        self.styleFrame = tk.Frame(self, background="#363636")
        self.styleFrame.place(relx=0, rely=0, height=300, width=300)
    
    def successful(self):
        self.destroy()
        self = ClientMonitor()

class ClientMonitor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{int(self.root.winfo_screenwidth()/1.5)}x{int(self.root.winfo_screenheight()/1.5)}")
        self.root.title("PyMonitor Client 0.1")
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

        self.exit =tk.Button(self.notificationFrame, text="Exit", background="#d60000", foreground="#d9d9d9", relief="groove", command=lambda: self.destroy())
        self.exit.place(relx=0.949, rely=0.05, relheight=0.9, relwidth=0.05)

    def main(self):
        self.mainFrame = tk.Frame(self, background="#363636")
        self.mainFrame.place(relx=0, rely=0.05, relheight=0.95, relwidth=1)
