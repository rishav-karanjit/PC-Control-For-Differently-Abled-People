import pyttsx3
import nltk
import wikipedia
import mysql.connector
import sys
import warnings

from Classes.News import News
from Classes.Internet_Search import Search
from Classes.DateAndTime import DateAndTime 
from Classes.SpeechRecog import Command 
from Classes.Greeting import GreetMe
from Classes.SysInfo import GetSys
from Classes.WordOp import Word

flag = 0
if not sys.warnoptions:
    warnings.simplefilter("ignore")

db = mysql.connector.connect(host='localhost',user='root',password='root',database='PCcontrol')
cursor = db.cursor()

class controller:
    def __init__(self):
        self.engine = pyttsx3.init()

    def Speak(self,audio):
        print(audio)      
        self.engine.say(audio)
        self.engine.runAndWait()

    def AskDate(self):
        Ctr.Speak("Today's date is")
        Ctr.Speak(DT.DateNow())

    def AskTime(self):
        Ctr.Speak("Current time is")
        Ctr.Speak(DT.TimeNow())

    def option(self,query):
        if "can you" in query:
            Ctr.Speak(Greet.Ans_Yes())

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

        elif "cpu" in query:
            Ctr.Speak(SystemInfo.GetCpu())

        elif "battery" in query:
            Ctr.Speak(SystemInfo.GetBattery())

        elif "write" in query:
            self.WordWCtr()

        elif "read" in query:
            self.WordRCtr()

        elif "no" in query:
            Ctr.Speak("Ending the program")
            quit()
        else:
            Ctr.Speak("Say that again please")

    def WordWCtr(self):
        flag = 1
        while(1):
            if(flag):
                Ctr.Speak("I can write a heading for you or a paragraph what do you want?")
            else:
                Ctr.Speak("I can your save or write one more heading or paragraph")

            HorP = Com.TakeCommand().lower()
            if "paragraph" in HorP:
                Ctr.Speak("What do you want me to write?")
                Write = Com.TakeCommand()
                Word.WAddPara(Write)
                Ctr.Speak("Paragraph written")
                flag = 0

            elif "save" in HorP:
                Ctr.Speak("What shall I name the file")
                FileName = Com.TakeCommand()
                Word.SaveWrittenTxt(FileName)
                return

            else:
                Ctr.Speak("What do you want me to write?")
                Write = Com.TakeCommand()
                flag = 0
                Ctr.Speak("Heading written.")

    def WordRCtr(self):
        Ctr.Speak("What is the name of file you want me to read")
        FileName = Com.TakeCommand()
        Ctr.Speak("This is what I found in the file:")
        Ctr.Speak(Word.WReadAll(FileName))
 
try:
    cursor.execute('SELECT * FROM userinfo')
    name = cursor.fetchone()[0]
except:
    name = False

Ctr = controller()
Greet = GreetMe()
Com = Command()
DT = DateAndTime()
S = Search()
N = News()
SystemInfo = GetSys()
Word = Word()

if name:
    Ctr.Speak(Greet.Welcome(name))
else:
    Ctr.Speak(Greet.Welcome(name))
    name = str(Com.TakeCommand())
    name = '\"' + name + '\"'
    cursor.execute('INSERT INTO userinfo(Name) VALUES({name})'.format(name=name))
    db.commit()
while(1):
    if flag == 1:
        Ctr.Speak("Do you have any more commands?")
    flag = 1
    query = Com.TakeCommand().lower()
    Ctr.option(query)