from snowboy import snowboydecoder
import speech_recognition as sr
from mycommands import commands
r = sr.Recognizer()

def detected_callback():
    print("hotword detected")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say Something : ")
        audio = r.listen(source)
        command = r.recognize_google(audio)
        print(command)
        commands(command)

detector = snowboydecoder.HotwordDetector("/home/saikiran/Documents/Projects/kingspeech/snowboy/resources/models/computer.umdl", sensitivity=0.5, audio_gain=1)
detector.start(detected_callback)
