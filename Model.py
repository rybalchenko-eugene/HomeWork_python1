from Note import Note

class Model():
    
    def __init__(self) -> None:
        pass

    def newNote(self):
        title = input("Введите заголовок заметки: ")
        text = input("Введите текст заметки: ")
        note = Note(title, text)
        return note
    
    def contentNote(self, repo):
        print("количество записей = ", len(repo))
        num = int(input("Введите номер ID заметки: "))
        print("количество записей = ", len(repo), "Выбор = ", num)
        if int(num) > len(repo)-1:
            print("Неверный ID")
        else:         
            print("Id = ", num) 
            print(repo[num].getTitle())     
            print(repo[num].getText()) 
            print(repo[num].getDate()) 

    def delNote(self, repo):
        print("количество записей = ", len(repo))
        num = int(input("Введите номер ID заметки: "))

        if int(num) > len(repo)-1:
            print("Неверный ID\n")
        else:         
            repo.pop(num)
        return repo
      

    
    