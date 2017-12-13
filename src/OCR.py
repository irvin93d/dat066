""" Recognize characters from image.
    Currently just a wrapper for pytesseract.
"""
import re
import pytesseract
import cv2
import numpy
from PIL import Image

def image_to_string(image):
    """ Return string of text from given image
    """
    # Turn image into array
    processed = numpy.array(image)

    # Grayscale
    processed = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)

    processed = cv2.adaptiveThreshold(processed,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,19,6)


    # Turn processed image back to image format
    processed = Image.fromarray(numpy.array(processed))
    text = pytesseract.image_to_string(processed)

    # Remove single newlines (always removes one newline in a group)
    text = re.sub('\n(?!\n)', ' ', text)
    # Remove multiple Newline
    text = re.sub('\n+', '\n', text)
    # Remove multiple space
    text = re.sub('[ \t]+', ' ', text)

    return text
