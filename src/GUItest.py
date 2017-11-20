import tkinter as tk
from tkinter import *
import ctypes
from PIL import Image
from PIL import ImageTk
import cv2

global picture_file_path
picture_file_path = 'face.jpg'

def __init__():
    create_window(800, 600)


def create_window(x_length_window, y_length_window):
    """Creates a Window with the size as input (x size, y size)
       createwindow(200,200) will a create a window 200x200px
    """

    global window
    window = tk.Tk()
    window.title("GUI Title V.1.0")
    screen_size = get_screen_resolution()

    x_window_position = str(int(screen_size[0] / 2 - (x_length_window / 2)))
    y_window_position = str(int(screen_size[1] / 2 - (y_length_window / 2)))
    window.geometry("800x600+" + x_window_position + "+" + y_window_position)

    menubar = Menu(window)
    options = Menu(menubar, tearoff=0)
    help_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Options", menu=options)
    options.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="Information", command=window.quit)
    window.config(menu=menubar)

    #viewframe = Frame(window, bg='black', width=xSize, height=ySize - 60)
    #image = ImageTk.PhotoImage(Image.open(path))
    img = load_image(picture_file_path);
    picture_label = Label(window, image = img)
    #view_frame.pack(side=TOP)
    picture_label.pack(side="top")

    button_frame = Frame(window, width=x_length_window, height=int(float(y_window_position) * 0.2), bg='white')
    button_frame.pack(side=BOTTOM)

    camera_button = Button(button_frame, text='Capture', fg="white", bg='red', width=15, height=3
                          , command=lambda: capture_image())
    camera_button.pack()

    tk.mainloop()


def get_screen_resolution():
    """Returns the screen resolution of the used device
    """
    screen_size = window.winfo_screenwidth(), window.winfo_screenheight()
    return screen_size


def capture_image():
    """Captures an image
    """
    print("Capture Image invoked")


def scale_image(original_image):
    pass


def load_image(filename):
    """Loads an image and returns it, it takes
    file path as input"""

    path = filename
    img = ImageTk.PhotoImage(Image.open(path))
    return img

__init__()
