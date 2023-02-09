from Note import Note

class Model():
    
    def __init__(self) -> None:
        pass

    def newNote(self):
        title = input("Введите заголовок заметки: ")
        text = input("Введите текст заметки: ")
        note = Note(title, text)
        return note
    

    
    