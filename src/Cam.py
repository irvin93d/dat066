""" Capture images from Webcamera
"""
import cv2
from PIL import Image

class Cam():
    """ Capture images from Webcamera
    """
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    def __del__(self):
        # TODO if not released
        self.cap.release()
    def start(self):
        # TODO Implement
        pass
    def capture(self):
        """ Capture current frame and return as Image
        """
        # TODO Test if successful
        ret, frame = self.cap.read()
        frame = Image.fromarray(frame)
        return frame
    def stop(self):
        # TODO Implement
        pass
