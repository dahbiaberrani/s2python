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






