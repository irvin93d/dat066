# dat066
Use camera to recognize a text and play it as audio.

## Description
Takes an photo with devices camera and processing it using OpenCV. The image is
then passed through Tesseract and turned into string format. The string
is played using Google's Text-To-Speech API (gTTS).

## Prerequisites
Required libraries: OpenCV and Tesseract
Required python packages: pytesseract, gTTS and tkinter.

### Install OpenCV on Linux
Follow instructions here: https://www.learnopencv.com/install-opencv3-on-ubuntu/  
Note that there may be issues running opencv with Anaconda3 (if you don't
know what Anaconda is, you are probably not using it).

### Install Tesseract on Linux
```
  sudo apt-get install tesseract-ocr
```

### Install libraries using pip
Expects you to have opencv installed according to instructions above.
Before installing packages, one must be using opencv virtual environment,
as used in instructions for installing OpenCV.
```
  workon facecourse-py3
```

To install package, run
```
  pip install <package>
```

## Usage

## Contributors
Duane Irvin  
076-026 00 26  
irvin93d@gmail.com  
duane@student.chalmers.se  

Pontus Karlsson  
073-507 11 15  
95poka78@gmail.com  
ponkarls@student.chalmers.se  

Jesper Holm  
076-310 85 11  
jstholm@gmail.com  
holmje@student.chalmers.se  

Aditya Subramanian  
073-074 06 12  
subramanianaditya42@gmail.com  

<!-- TODO ## License-->
