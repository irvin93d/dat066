""" Recognize characters from image.
    Currently just a wrapper for pytesseract.
"""
import re
import pytesseract

def image_to_string(image):
    """ Return string of text from given image
    """
    text = pytesseract.image_to_string(image)

    # Remove single newlines (always removes one newline in a group)
    text = re.sub('\n(?!\n)', '', text)
    # Remove multiple Newline
    text = re.sub('\n+', '\n', text)
    # Remove multiple space
    text = re.sub('[ \t]+', ' ', text)


    

    return text
