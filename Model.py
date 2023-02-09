from Note import Note

class Model():
    
    def __init__(self) -> None:
        pass

    def newNote(self):
        title = input("Введите заголовок заметки: ")
        text = input("Введите текст заметки: ")
        note = Note(title, text)
        print("Заметка успешно создана\n")
        return note
    
    def contentNote(self, repo):
        num = int(input("Введите номер ID заметки: "))
        if int(num) > len(repo)-1:
            print("Неверный ID\n")
        else:         
            print("Id = ", num) 
            print("Заголовок: ",repo[num].getTitle())     
            print("Содержание: ",repo[num].getText()) 
            print("Дата создания: ",repo[num].getDate()) 

    def delNote(self, repo):
        print("количество записей = ", len(repo))
        num = int(input("Введите номер ID заметки: "))
        if int(num) > len(repo)-1:
            print("Неверный ID\n")
        else:         
            repo.pop(num)
            print("Заметка удалена\n")
        return repo
      
    def editNote(self, repo):
        print("количество записей = ", len(repo))
        num = int(input("Введите номер ID заметки: "))
        if int(num) > len(repo)-1:
            print("Неверный ID\n")
        else:         
            title = input("Введите заголовок заметки: ")
            text = input("Введите текст заметки: ")
            note = Note(title, text)
            repo[num] = note
            print("Заметка успешно отредактирована\n")
        return repo
    
    