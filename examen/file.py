class File:
    def __init__(self,maxMafile):
        self.maxfile = maxMafile
        self.contenu = []


    def __str__(self):
        return str(self.contenu)

    def afficher(self):
        print(self)
    
    def fileVide(self):
        if len(self.contenu) == 0:
            return True
        else:
            return False

    def filepleine(self):
        return  len(self.contenu) ==  self.maxfile 
            
    def ajouter(self,elt):
        if self.filepleine():
            print("impossible d'ajouter un elt la liste est pleine ")
        else:
            self.contenu.append(elt)
      
    def retirer(self):
        if self.fileVide():
            print("impossible de retirer un elt la liste est vide ")
        else:
            tmp = self.contenu[0]
            self.contenu.remove(tmp)
            return tmp
    
    def maxSize(self):
        return self.maxfile


def reverseFile(file):
    newFile = File(file.maxSize())
    tab = []
    while not file.fileVide():
        elem = file.retirer()
        tab.append(elem)
    for i in range (len(tab)):
        newFile.ajouter(tab[len(tab)-1-i])
    return newFile  


# test 
f1 = File(10)
f1 .ajouter (1)
f1 .ajouter (2)
f1 .ajouter (3)
f1 .ajouter (4)
f1 .ajouter (5)
print(f1)
f2 = reverseFile(f1)
print(f2)





