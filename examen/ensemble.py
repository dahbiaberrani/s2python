class Ensemble:
    def __init__(self):
        self.contenu =[]            #contenu de l'ensemble initialisée par tableau vide []

    def __str__(self):
        return str(self.contenu)

    #ajoute e à l’ensemble, si e est déjà présent, renvoie une erreur ;
    def ajouter(self, e) : 
        if e1.present(e):
            print("L'element est déjà existant\n")
            return None
        else : 
            self.contenu.append(e)




    # renvoie l’élément à l’index i de l’ensemble ;
    def at_index(self, i) : 
        if i < 0 or i  > self.taille() -1:
            print("index inexistant\n")
            return None
        else :
            return self.contenu[i]

    # renvoie le nombre d’éléments contenus dans l’ensemble ;
    def taille (self) :
        return len(self.contenu)

    # renvoie Vrai si l’ensemble est vide, Faux sinon ;
    def estVide(self) : 
        return len(self.contenu) == 0
    # renvoie Vrai si e est dans l’ensemble, Faux sinon.
    def present(self, e) : 
        return e in self.contenu

    # retire e de l’ensemble, si e n’est pas présent, renvoie une erreur ;
    def retirer(self, e) : 
        if self.present(e):
            # recherche de l'index
            i = self.contenu.index(e)
            self.contenu.pop(i)

