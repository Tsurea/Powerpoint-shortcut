import psutil
import pyautogui, os
import win32com.client
import win32api

class Power:
    def __init__(self):
        pass

    def appRunning(self):
        res = []

        for p in psutil.process_iter():
            res.append(p.name())

        return res

    def add_file(self, file):
        Application = win32com.client.Dispatch('PowerPoint.Application')
        
        presentation = Application.Presentations.Open(Filename=file)
        slide = presentation.Slides.Add(1, LAYOUT_BLANK)

class Recorder:
    def __init__(self):
        self.special_keys = [0x01, 0x02, 0x10, 0x20]

        self.special = {
            0x01: 'leftClick',
            0x02: 'rightClick',
            0x10: 'shift',
            0x20: 'space'
        }

    def key_down_time(self, key):
        pass

    def pressing(self):
        sleep(1)
        while True:
            for i in range(2, 256):
                if win32api.GetAsyncKeyState(i):
                    return i

if __name__ == "__main__":
    Power().appRunning()