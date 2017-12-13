""" Turn text into speech
"""
import tempfile
from pygame import mixer
from gtts import gTTS

class TTS():
    """ Wrapper for gtts and mixer (module used to play mp3 from gtts)
    """
    def __init__(self):
        mixer.init()

    @staticmethod
    def say(text):
        """ Play text. Interrupt currently playing text if any is playing
        """
        if mixer.music.get_busy():
            mixer.music.stop()
        tts = gTTS(text=text, lang='en-us')
        tmp = tempfile.mktemp(suffix='mp3')
        tts.save(tmp)
        mixer.music.load(tmp)
        mixer.music.play()
