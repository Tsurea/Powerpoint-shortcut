import tkinter as tk
from PIL import ImageTk, Image
import pyglet

class Interface:
    def __init__(self):
        self.window = tk.Tk()

        self.window.title("DJL Training")
        self.window.geometry("700x400")
        self.window.resizable(1, 1)

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
        pyglet.font.add_file('Bangers-Regular.ttf')
        tk.Label(self.frame[0], text='DJL TRAINING', font=("Bangers-Regular", 20), fg='#0A6EE4').place(relx=.5, rely=0, relwidth=0.5, relheight=0.4)

    def create_captureFrame(self):
        self.frame[1]['bg'] = '#0A6EE4'
        self.frame[1].place(relx=0, rely=0.4, relwidth=1, relheight=0.2)

        tk.Label(self.frame[1], text="App to Capture", fg="white", bg='#0A6EE4', font=("Courrier", 13)).place(relx=0, rely=0, relwidth=0.3, relheight=1)

        self.menubutton = tk.Menubutton(self.frame[1], text="Choose your app")
        self.menubutton.menu = tk.Menu(self.menubutton)
        self.menubutton["menu"] = self.menubutton.menu

        self.menubutton.menu.add_command(label="APP", command=lambda: print("app"))
        self.menubutton.menu.add_command(label='Yo', command=lambda: print('yo'))

        self.menubutton.place(relx=0.301, rely=.25, relwidth=0.3, relheight=0.5)

        tk.Label(self.frame[1], text='Hotkey', fg="white", bg='#0A6EE4', font=("Courrier", 12)).place(relx=0.7, rely=.25, relwidth=0.08, relheight=0.5)
        tk.Button(self.frame[1], text='Click', font=("Courrier", 10)).place(relx=.8, rely=.25, relwidth=0.17, relheight=.5)
        
    def create_fileFrame(self):
        self.frame[2]['bg'] = '#FF5500'
        self.frame[2].place(relx=0, rely=0.61, relwidth=1, relheight=0.2)

        tk.Label(self.frame[2], text="PowerPoint File", fg="white", bg='#FF5500', font=('Courrier', 13)).place(relx=0, rely=0, relwidth=0.3, relheight=1)

        self.entry = tk.Entry(self.frame[2], font=('Courrier', 12))
        self.entry.place(relx=0.301, rely=0.25, relwidth=0.55, relheight=0.5)

        self.chooseExe = tk.Button(self.frame[2], text="...")
        self.chooseExe.place(relx=.87, rely=0.25, relwidth=0.1, relheight=.5)


    def create_startFrame(self):
        self.frame[3].place(relx=0, rely=0.81, relwidth=1, relheight=0.19)

        self.button = tk.Button(self.frame[3], text="Start", width=20, height=2, font=("Courrier", 12))
        self.button.pack(expand=tk.YES)

if __name__ == "__main__":
    Interface()