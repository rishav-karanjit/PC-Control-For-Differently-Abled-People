import pyttsx3
from DateAndTime import DateAndTime 
from Greeting import GreetMe

class controller:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self,audio):      
        self.engine.say(audio)
        self.engine.runAndWait()

    def AskDate(self):
        C.speak("Date is")
        C.speak(DT.DateNow())

    def AskTime(self):
        C.speak("Time is")
        C.speak(DT.TimeNow())


C = controller()
DT = DateAndTime()
Greet = GreetMe()

C.speak(Greet.Welcome())