"""pyttsx3 is the engine for TTS"""
import pyttsx3

class TTS():
    """Text-to-Speech

    Use pyttsx3 to play a voice from a text string

        :Example:
        tts = TTS()
        tts.say("Hey there!")

    """
    def __init__(self):
        self.engine = pyttsx3.init()
        """ TODO set volume and language """

    def say(self, text):
        """play string text from speakers"""
        # TODO Test that text is a string
        self.engine.say(text)
        self.engine.runAndWait()
