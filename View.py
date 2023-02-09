class View:
    def __init__(self) -> None:
        pass
    
    def userInput(self):
        print("Выберите пункт меню:")
        print("1. Создать запись")
        print("2. Вывести список заголовков записей")
        print("3. Вывести запись по ID")
        print("4. Загрузить список записей из файла")
        print("5. Сохранить запись в файл")
        
        user_input = input("Введите пункт меню...")
        return user_input


        
    