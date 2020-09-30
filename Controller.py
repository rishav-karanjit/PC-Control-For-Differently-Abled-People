import pyttsx3
import nltk
import wikipedia

from Classes.News import News
from Classes.Internet_Search import Search
from Classes.DateAndTime import DateAndTime 
from Classes.SpeechRecog import Command 
from Classes.Greeting import GreetMe
from Classes.SysInfo import GetSys

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

    def option(self,query):
        if "Can you" in query:
            Greet.Ans_Yes()

        if "date" in query:
            Ctr.AskDate()

        elif "wikipedia" in query:
            query = query.replace('wikipedia','')
            Ctr.Speak(S.Wiki_Result(query))

        elif "news" in query:
            Ctr.Speak("Here are top news in the Internet")
            self.engine.setProperty('rate', 170)
            Ctr.Speak(N.GetTopNews())
            self.engine.setProperty('rate', 200)

        elif "CPU" in query:
            Ctr.Speak(SystemInfo.GetCpu())
        else:
            Ctr.Speak("Say that again please")

Ctr = controller()
Greet = GreetMe()
# Ctr.Speak(Greet.Welcome())

Com = Command()
query = Com.TakeCommand().lower()
DT = DateAndTime()
S = Search()
N = News()
SystemInfo = GetSys()
Ctr.option(query)