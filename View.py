class View:
    def __init__(self) -> None:
        pass
    
    def userInput(self):
        print("\nВыберите пункт меню:")
        print("1. Создать запись")
        print("2. Вывести список заголовков записей")
        print("3. Вывести запись по ID")
        print("4. Загрузить список записей из файла")
        print("5. Сохранить запись в файл")
        print("6. Удалить заметку по ID")
        print("7. Редактировать заметку по ID")     
        print("0. Выход\n")    
        user_input = input("Введите пункт меню...")
        return user_input

    def viewList(self, repo):
        for i in range(0,len(repo)):
            print("ID =", i,"->",repo[i].getTitle())

        
    