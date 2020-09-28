import speech_recognition as sr

class Command:
    def TakeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening ...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing ...")
            query = r.recognize_google(audio,language = 'en-US')
            print(query)
        
        except Exception as e:
            print(e)
            print("Say that again please")
            query = "Say that again please"
        return query


        