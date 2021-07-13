from gtts import gTTS
from audioplayer import AudioPlayer
import pyttsx3

#Text to speech using Google Text-to-Speech API
def text_to_speech1(label):
    #Converting text to speech
    tts=gTTS(text=label, lang='en', slow=False)
    #Saving the converted audio file into the same directory
    tts.save("Outputs/output.mp3")
    #Play the converted file
    AudioPlayer("Outputs/output.mp3").play(block=True)

def text_to_speech(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
