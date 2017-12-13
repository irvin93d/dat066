
import os
import OCR
import difflib
from PIL import Image

data_folder = "data/"

def remove_extension(x):
    return(os.path.splitext(x)[0])

def get_accuracy(x,y):
    diff = [d for d in difflib.ndiff(x, y)]
    correct = [d for d in diff if d[0] == ' ']
    return len(correct) / len(diff)


for data_name in set(map(remove_extension, os.listdir(data_folder))):
    image_path = data_folder + data_name + ".png"
    txt_path = data_folder + data_name + ".txt"

    if not os.path.isfile(image_path):
        print(data_name, "has no image")
        continue
    if not os.path.isfile(txt_path):
        print(data_name, "has no txt")
        continue
    image = Image.open(image_path, 'r')
    txt = None
    with open(txt_path, 'r') as f:
        txt = f.read()

    rec = OCR.image_to_string(image)

    print("Accuracy:\t", round(get_accuracy(txt, rec), 2), "\t", data_name)
