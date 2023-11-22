import pyttsx3
import gtts
from PyPDF2 import PdfReader
from playsound import playsound
from openai import OpenAI

api_key = " "
client = OpenAI(api_key=api_key)

#Google TSS

tss = gtts.gTTS("My name is Simon and I like to do drawings.")

tss.save("simon.mp3")

playsound("simon.mp3")

# in spanish
tts = gtts.gTTS("Hola.  Donde es la escuela?", lang="es")
tts.save("hola.mp3")
playsound("hola.mp3")

#Pytssx3

engine = pyttsx3.init()
text = "Pleased to meet you.  Hope you guess my name."
engine.say(text)
engine.runAndWait()

engine.save_to_file(text, "devil.aiff")
engine.runAndWait()

#Open AI

# sample text to generate speech from
text = """Robert Clark Seger is a retired American singer, songwriter, and musician. 
As a locally successful Detroit-area artist, he performed and recorded as Bob Seger and 
the Last Heard and the Bob Seger System throughout the 1960s, breaking through with his 
first album, Ramblin' Gamblin' Man  in 1969."""

# generate speech from the text
response = client.audio.speech.create(
    model="tts-1", # the model to use, there is tts-1 and tts-1-hd
    voice="nova", # the voice to use, there is alloy, echo, fable, onyx, nova, and shimmer
    input=text, # the text to generate speech from
    speed=1.0, # the speed of the generated speech, ranging from 0.25 to 4.0
)
# save the generated speech to a file
response.stream_to_file("seger.mp3")










