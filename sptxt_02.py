import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()

def gettext():
    with sr.Microphone() as source1:
        r.adjust_for_ambient_noise(source1, duration = 0.2)
        audio1 = r.listen(source1)
        textdata = r.recognize_google(audio1)
        textdata = textdata.lower()
        print("Answer:-  " + textdata)
        
print("What is your name?")
gettext()

print("What is your hobby?")
gettext()
   
print("What time is it?")
gettext()
