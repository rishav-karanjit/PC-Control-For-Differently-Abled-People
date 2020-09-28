import pyttsx3
import nltk
import wikipedia

from DateAndTime import DateAndTime 
from SpeechRecog import Command 
from Greeting import GreetMe

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
        tokens = nltk.word_tokenize(query)
        tagged = nltk.pos_tag(tokens)
        for i in tagged:
            if i[1] is NN or NNS:
                print(i[0])

    else:
        Ctr.Speak("Say that again please")

Ctr = controller()
Greet = GreetMe()
Ctr.Speak(Greet.Welcome())


Com = Command()
query = Com.TakeCommand().lower()
DT = DateAndTime()

option(query)