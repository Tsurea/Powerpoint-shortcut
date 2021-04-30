import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter import messagebox

from time import sleep
from threading import Thread
import pyglet

from power import Power, Recorder

class Interface:
    def __init__(self):
        self.record = Recorder()
        self.power = Power()
        self.window = tk.Tk()

        self.window.title("DJL Training")
        self.window.geometry("700x450")
        self.window.iconbitmap('assets/powerpoint.ico')
        self.window.resizable(0, 0)
        self.window.config(bg="#FFFFFF")

        self.frame = [tk.Frame(self.window) for i in range(4)]

        self.create_widgets()

        self.window.mainloop()

    def create_widgets(self):
        self.create_nameFrame()
        self.create_captureFrame()
        self.create_fileFrame()
        self.create_startFrame()

    def create_menu(self):
        pass

    def create_nameFrame(self):
        self.frame[0].place(relx=0, rely=0, relwidth=1, relheight=0.4)

        self.photo = tk.PhotoImage(file='./assets/SmileShot.png').subsample(2, 2)
        self.Artwork = tk.Button(self.frame[0], text='Press to reset', image=self.photo, highlightthickness=0, bd=0)
        self.Artwork.photo = self.photo
        self.Artwork.place(relx=0.1, rely=0, relwidth=0.3, relheight=1)
        
        pyglet.font.add_file('myFont.ttf')
        tk.Label(self.frame[0], text='DJL TRAINING', font=("Bangers", 36), fg='#0A6EE4').place(relx=.45, rely=0.2, relwidth=0.5, relheight=0.4)
        
        tk.Label(self.frame[0], text='Screenshot to PowerPoint', font=('Helvetica', 20), fg='#FF5500').place(relx=.445, rely=0.6, relwidth=0.525, relheight=.2)

    def create_captureFrame(self):
        self.frame[1]['bg'] = '#0A6EE4'
        self.frame[1].place(relx=0, rely=0.4, relwidth=1, relheight=0.2)

        tk.Label(self.frame[1], text="App to Capture", fg="white", bg='#0A6EE4', font=("Courrier", 13)).place(relx=0, rely=0, relwidth=0.3, relheight=1)

        self.searchBar = tk.Entry(self.frame[1], font=('Courrier', 13))
        self.searchBar.place(relx=0.301, rely=.15, relwidth=0.3, relheight=0.3)

        self._list = tk.Listbox(self.frame[1])
        self._list.place(relx=0.301, rely=.60, relwidth=0.3, relheight=0.3)

        self.update(self.power.appRunning())

        self._list.bind("<<ListboxSelect>>", self.fillout)
        self.searchBar.bind("<KeyRelease>", self.check)

        tk.Label(self.frame[1], text='Hotkey', fg="white", bg='#0A6EE4', font=("Courrier", 12)).place(relx=0.69, rely=.25, relwidth=0.09, relheight=0.5)
        
        self.keyblinder = tk.Button(self.frame[1], text='Click', font=("Courrier", 10), command=lambda: Thread(target=self.chooseHotkey).start())
        self.keyblinder.place(relx=.8, rely=.25, relwidth=0.17, relheight=.5)
        
    def create_fileFrame(self):
        self.frame[2]['bg'] = '#FF5500'
        self.frame[2].place(relx=0, rely=0.61, relwidth=1, relheight=0.2)

        tk.Label(self.frame[2], text="PowerPoint File", fg="white", bg='#FF5500', font=('Courrier', 13)).place(relx=0, rely=0, relwidth=0.3, relheight=1)

        self.entry = tk.Entry(self.frame[2], font=('Courrier', 10))
        self.entry.place(relx=0.301, rely=0.25, relwidth=0.55, relheight=0.5)

        self.chooseExe = tk.Button(self.frame[2], text="...", command=self.chooseFile)
        self.chooseExe.place(relx=.87, rely=0.25, relwidth=0.1, relheight=.5)


    def create_startFrame(self):
        self.frame[3].place(relx=0, rely=0.81, relwidth=1, relheight=0.19)

        self.button = tk.Button(self.frame[3], text="Start", width=20, height=2, font=("Courrier", 12), command=self.start)
        self.button.pack(expand=tk.YES)
    
    def start(self):
        # First check if their is no problem
        if self.entry.get() == '':
            messagebox.showerror("No file select", 'You need to choose a file')
            return
        elif self.keyblinder['text'] == 'Click':
            messagebox.showerror('No key choosing', 'You have to choose a key')
            return
        elif self.searchBar['text'] in self.power.appRunning():
            messagebox.showerror('App not open', 'You have to choose an app that is open')
            return
        else:
            print("everything is awesome")
    def chooseFile(self):
        filename = askopenfile()
        print(filename.name)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, filename.name)

    def chooseHotkey(self):

        self.keyblinder['text'] = "Click the touch"
   
        self.hotkey = self.record.pressing()

        if self.hotkey in self.record.special_keys:
            self.keyblinder['text'] = self.record.special[self.hotkey]
        else:
            self.keyblinder['text'] = chr(self.hotkey)
    
    # Update the listbox
    def update(self, data):
        self._list.delete(0, tk.END)
        
        for item in data:
            self._list.insert(tk.END, item)
    
    def fillout(self, event):
        self.searchBar.delete(0, tk.END)

        self.searchBar.insert(0, self._list.get(tk.ACTIVE))
    
    def check(self, event):
        typed = self.searchBar.get()

        if typed == '':
            data = self.power.appRunning()
        else:
            data = []
            for item in self.power.appRunning():
                if typed.lower() in item.lower():
                    data.append(item)

        self.update(data)
if __name__ == "__main__":
    Interface()