import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
'''with sr.Microphone as source2:
    audiotext = r.listen(source)
    try:
        text = r.recognize_google(audiotext)
        print(text)
    except:
        print(exception)'''
while(1):
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration = 0.2)
        audio2 = r.listen(source2)
        textdata = r.recognize_google(audio2)
        textdata = textdata.lower()
        print("Did you say   " + textdata)
        
