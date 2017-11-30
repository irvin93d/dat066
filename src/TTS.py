import tempfile
from pygame import mixer
from gtts import gTTS

class TTS():
    def __init__(self):
        mixer.init()

    def say(self, text):
        if mixer.music.get_busy():
            mixer.music.stop()
        tts = gTTS(text=text, lang='en-us', slow=True)
        tmp = tempfile.mktemp(suffix='mp3')
        tts.save(tmp)
        mixer.music.load(tmp)
        mixer.music.play()
