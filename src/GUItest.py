import tkinter as tk
from tkinter import *
import ctypes
from PIL import Image
from PIL import ImageTk
import cv2

def __init__():
    createwindow(800, 600)


def createwindow(xSize, ySize):
    """Creates a Window with the size as input (x size, y size)
       createwindow(200,200) will a create a window 200x200px
    """

    window = tk.Tk()
    window.title("GUI Title V.1.0")
    screen = getscreenresolution()
    xPos = str(int(screen[0] / 2 - (xSize / 2)))
    yPos = str(int(screen[1] / 2 - (ySize / 2)))
    window.geometry("800x600+" + xPos + "+" + yPos)

    menubar = Menu(window)
    options = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Options", menu=options)
    options.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="Information", command=window.quit)
    window.config(menu=menubar)

    viewframe = Frame(window, bg='black', width=xSize, height=ySize - 60)
    path = 'face.jpg'
    image = cv2.imread(path)
    picturepanel = Label(viewframe)
    picturepanel.image = image
    picturepanel.pack()
    viewframe.pack(side=TOP)

    buttonframe = Frame(window, width=xSize, height=int(float(yPos) * 0.2), bg='white')
    buttonframe.pack(side=BOTTOM)

    camerabutton = Button(buttonframe, text='Capture', fg="white", bg='red', width=15, height=3
                          , command=lambda: captureimage())
    camerabutton.pack()

    tk.mainloop()


def getscreenresolution():
    """Returns the screen resolution of the used device
    """
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return screensize


def captureimage():
    """Captures an image
    """
    print("Capture Image invoked")


__init__()
