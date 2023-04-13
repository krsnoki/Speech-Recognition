#import tkinter as tk
import speech_recognition as sr
import pyttsx3
import mysql.connector
from gtts import gTTS
from playsound import playsound
r = sr.Recognizer()
top = tk.Tk()
top.config(bg = "Yellow")
top.geometry("600x600")

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "chatbox")
mycur = mydb.cursor()
newn = ""
name = 100000

def give_name(sp):
    l = 'en'
    obj = gTTS(text = sp, lang = l, slow = False)
    global name
    global newn
    
    mycur.execute("select * from chat2")
    result = mycur.fetchall()
    newf = ""
    for x in result:
        newf = x[0]
    newn = (str(name) + str(newf) + ".mp3")
    obj.save(newn)
    return newn




def getnstore(ans, txt):
        query = "insert into chat2(Question, Answer)values(%s, %s)"
        values = (txt, ans)
        mycur.execute(query, values)
        mydb.commit()
        print("Stored....well")

        
        
mycur.execute("Select Question from chat")
result = mycur.fetchall()

for x in result:
    print(x[0])
    with sr.Microphone() as source1:
        r.adjust_for_ambient_noise(source1, duration = 0.2)
        audio1 = r.listen(source1)
        textdata = r.recognize_google(audio1)
        textdata = textdata.lower()
        print("\n Answer:-  "+ textdata)
        
        getnstore(textdata, x[0])
        text = gTTS(text = textdata, lang = 'en', slow = False)
        clip = give_name(textdata)
        text.save(clip)
        playsound(clip)
   










