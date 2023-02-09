import json
from Note import Note

def saveRepo(repo):
    filename = 'Notesrepo.json'
    repo_temp = {}
    
    for i in repo:
        note = repo[i].getTitle() + "|" + repo[i].getText() + "|" + str(repo[i].getDate())
        repo_temp[i] = note        
    with open(filename, 'w') as f:
        json.dump(repo_temp, f)
        
def loadRepo():
    try:
        filename = 'Notesrepo.json'
        with open(filename) as f:
            repo = json.load(f)
            repo_temp = {}
            for i in repo:
                note = str(repo[i])
                temp = note.split("|", 2)
                print(temp)
                repo_temp[i] = Note(temp[0], temp[1])
                repo_temp[i].setDate(temp[2])
                
            print(repo_temp)    
            return repo_temp
    except FileNotFoundError:
        print("Нет такого файла")
        
        