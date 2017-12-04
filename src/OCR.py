""" Recognize characters from image.
    Currently just a wrapper for pytesseract.
"""
import pytesseract
import re

def image_to_string(image):
    """ Return string of text from given image
    """
    text = pytesseract.image_to_string(image)

    # Remove Newline
    text = text.replace('\n', ' ')
    # Remove multiple space
    text = re.sub('[ \t]+', ' ', text)


    

    return text
