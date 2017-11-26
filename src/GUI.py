""" User Interface for Optical Character Recogntion Project
"""
import tkinter as tk
from PIL import ImageTk

class GUI(tk.Tk):
    """ User interface showing video stream
    """
    def __init__(self, key_handler, *args, **kdwargs):
        tk.Tk.__init__(self, *args, **kdwargs)
        self.title("Optical Character Recognition")
        self.panel = None
        self.image = None
        self.bind("<Key>", key_handler)

    def set_frame(self, image):
        """ Sets the current frame of GUI
        """
        self.image = ImageTk.PhotoImage(image)
        if self.panel is None:
            self.panel = tk.Label(self, image=self.image)
        else:
            self.panel.configure(image=self.image)
        self.panel.pack(side="bottom", fill="both", expand="yes")
