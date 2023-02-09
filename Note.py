import datetime

class Note:

    
    def __init__(self, title, text) -> None:
        self.title = title
        self.text = text
        self.date = datetime.datetime.now()

    def getTitle(self):
        return self.title
    
    def getText(self):
        return self.text
    
    def getDate(self):
        return self.date
    
    def setDate(self, date):
        self.date = date

    
    
    
    