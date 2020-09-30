import pyttsx3
import nltk
import wikipedia

from Classes.Internet_Search import Search
from Classes.DateAndTime import DateAndTime 
from Classes.SpeechRecog import Command 
from Classes.Greeting import GreetMe

class controller:
    def __init__(self):
        self.engine = pyttsx3.init()

    def Speak(self,audio):      
        self.engine.say(audio)
        self.engine.runAndWait()

    def AskDate(self):
        Ctr.Speak("Today's date is")
        Ctr.Speak(DT.DateNow())

    def AskTime(self):
        Ctr.Speak("Current time is")
        Ctr.Speak(DT.TimeNow())

def option(query):
    if "date" in query:
        Ctr.AskDate()

    elif "wikipedia" in query:
        query = query.replace('wikipedia','')
        Ctr.Speak(S.Wiki_Result(query))
    else:
        Ctr.Speak("Say that again please")

Ctr = controller()
Greet = GreetMe()
# Ctr.Speak(Greet.Welcome())

Com = Command()
query = Com.TakeCommand().lower()
DT = DateAndTime()
S = Search()
option(query)