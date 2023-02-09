
from Model import Model
from View import View
from Saver import *

class Presenter():



    
    def __init__(self) -> None:
        pass

    def start(self):
        repo = []
        print("Hello, user. Notebook is working..")
        model = Model()
        view = View()

        while True:
            choice = view.userInput()
            if choice == "1":
                repo.append(model.newNote())
                print(repo)
            if choice == "2":
                view.viewList(repo)
            if choice == "3":  
                model.contentNote(repo)
            if choice == "4":
                repo = loadRepo()
            if choice == "5":
                saveRepo(repo)
            if choice == "6":
                repo = model.delNote(repo)
            if choice == "7":
                repo = model.editNote(repo)
            if choice == "0":
                exit(0)
        
        
        
    





