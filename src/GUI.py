import tkinter as tk
from PIL import ImageTk

class GUI(tk.Tk):
    def __init__(self, key_handler, *args, **kdwargs):
        tk.Tk.__init__(self, *args, **kdwargs)
        self.title("TITLE")
        self.panel = None
        self.image = None
        self.bind("<Key>", key_handler)
    def set_image(self, image):
        # Creates a Tkinter-compatible photo image,
        # which can be used everywhere Tkinter expects an image object.
        self.image = ImageTk.PhotoImage(image)
        if self.panel is None:
            self.panel = tk.Label(self, image=self.image)
        else:
            self.panel.configure(image=self.image)
        self.panel.pack(side="bottom", fill="both", expand="yes")
