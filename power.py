import psutil
import pyautogui, os

import win32gui
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
    
    def screenshot(self, app):
        '''
        This module do the screenshot of the choosed app.

        param app: str, name of the app
        '''
        # First get is position and size
        coordonnee = self.callback(app)

        image = pyautogui.screenshot('screenshot.png', region=coordonnee)


    def callback(self, window, extra):
        '''
        Get the position and size of the window.
        '''
        rect = win32gui.GetWindowRect(window)

        print(f'Window {win32gui.GetWindowText(window)}')
        print(f'x: {rect[0]}\ny: {rect[1]}\nw: {rect[2] - rect[0]}\nh: {rect[3] - rect[1]}')

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
    print(win32gui.EnumWindows(Power().callback, None))