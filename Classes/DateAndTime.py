import datetime

class DateAndTime:
    def TimeNow(self):
        return datetime.datetime.now().strftime("%H:%M:%S")

    def DateNow(self):
        return datetime.date.today()