from tkinter import *


class AwindowApp:
    def __init__(self, root):
        self.__window = root
        self.__n = 0
        self.__aButton = Button(self.__window)
        self.__aButton.config(text = "press me")
        self.__aButton.config(command = self.__oneHandler)
        self.__aButton.pack()
    def __oneHandler(self):
        print('oneHandled', self.__n)
        self.__n = self.__n + 1
        if self.__n < 2:
            self.__window.after(500, self.__anotherHandler)
            self.__window.after(200, self.__oneHandler)
    def __anotherHandler(self):
        print('anotherHandled')


root = Tk()
win = AwindowApp(root)
root.mainloop()