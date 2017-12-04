""" Recognize characters from image.
    Currently just a wrapper for pytesseract.
"""
import pytesseract

def image_to_string(image):
    """ Return string of text from given image
    """
    text = pytesseract.image_to_string(image)
    text = text.replace('\n', ' ')
    return text
