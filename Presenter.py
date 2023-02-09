
from Model import Model
from View import View
from Saver import *

class Presenter():



    
    def __init__(self) -> None:
        pass

    def start(self):
        repo = []
        id = 0
        print("Hello, user. Notebook is working..")
        model = Model()
        view = View()

        # print("Выберите пункт меню:")
        # print("1. Создать запись")
        # print("2. Вывести список заголовков записей")
        # print("3. Вывести запись по ID")
        # print("4. Загрузить список записей из файла")
        # print("5. Сохранить запись в файл")
        while True:
            choice = view.userInput()
            if choice == "1":
                repo.append(model.newNote())
                print(repo)
            if choice == "2":
                for i in range(0,len(repo)):
                    print("ID = ", i)
                    print(repo[i].getTitle())
            if choice == "3":  
                model.contentNote(repo)
            if choice == "4":
                repo = loadRepo()
            if choice == "5":
                saveRepo(repo)
            if choice == "6":
                repo = model.delNote(repo)
            if choice == "0":
                exit(0)
        
        
        
    





