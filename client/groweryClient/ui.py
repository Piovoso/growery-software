import tkinter as TK
import json as js, os

class Window:
    def __init__(self):
        with open(f"{os.path.dirname(__file__)}/meta/data.json") as file: data = js.load(file)
        self = TK.Tk()
        print()
        self.geometry(f'{int(self.winfo_screenwidth()/2)}x{int(self.winfo_screenheight()/2)}')
        self.resizable(0,0)
        self.title(f'PyMonitor {data["version"]}')
        self.mainloop()

Window()