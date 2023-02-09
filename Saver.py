import json
from Note import Note

def saveRepo(repo):
    filename = 'Notesrepo.json'
    repo_temp = []
    
    for i in range(0,len(repo)):
        note = repo[i].getTitle() + ";" + repo[i].getText() + ";" + str(repo[i].getDate())
        repo_temp.append(note)      
    with open(filename, 'w') as f:
        json.dump(repo_temp, f)
        print("Заметки успешно сохранены\n")
        
def loadRepo():
    
    try:
        filename = 'Notesrepo.json'
        with open(filename) as f:
            print("Существующий список заметок будет перезаписан!\n")
            repo = json.load(f)
            repo_temp = []
            for i in range(0,len(repo)):
                note = str(repo[i])
                temp = note.split(";", 2)
                print(temp)
                temp_note = Note(temp[0], temp[1])
                temp_note.setDate(temp[2])
                repo_temp.append(temp_note)
            return repo_temp
    except FileNotFoundError:
        print("Нет такого файла\n")
        
        