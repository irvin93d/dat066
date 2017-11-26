
import GUI
import Cam
import OCR
import TTS

class KeyHandler():
    def __init__(self):
        self.key_pressed = None
    def get_key(self):
        key = self.key_pressed
        self.key_pressed = None
        return key
    def key_event(self, event):
        self.key_pressed = event.keysym
        print("Keypressed:", event.keysym)
    k = False

def main():
    key_pressed = None
    frame = None

    key_handler = KeyHandler()
    cam = Cam.Cam()
    gui = GUI.GUI(key_handler.key_event)
    tts = TTS.TTS()

    while not key_pressed == "Escape":
        key_pressed = key_handler.get_key()
        frame = cam.capture()
        gui.set_frame(frame)
        gui.update_idletasks()
        gui.update()
        if key_pressed == "space":
            print("Capture")
            text = OCR.image_to_string(frame)
            print(text)
            tts.say(text)



if __name__ == "__main__":
    main()
