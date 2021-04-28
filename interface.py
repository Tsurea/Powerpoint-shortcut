import tkinter as tk
from PIL import ImageTk, Image

class Interface:
    def __init__(self):
        self.window = tk.Tk()

        self.window.title("DJL Training")
        self.window.iconbitmap("")
        self.window.resizable(0, 0)
        
        self.frame = tk.Frame(self.window)

        self.create_widgets()

        self.frame.pack(expand=tk.YES)
        
    def create_widgets(self):
        self.create_nameFrame()

    def create_menu(self):
        pass

    def create_nameFrame(self):
        self.nameFrame = tk.Frame(self.frame)
        self.nameFrame.place(relx=0, rely=0, relwidth=1, relheight=0.4)

        logo = ImageTk.PhotoImage(Image.open("assets/SmileShot.png"))
        panel = tk.Label(self.nameFrame, image=logo)
        panel.place(relx=0, rely=0, relwidth=0.5, relheight=1)

    def create_captureFrame(self):
        pass

    def create_fileFrame(self):
        pass

    def create_startFrame(self):
        pass
if __name__ == "__main__":
    Interface()