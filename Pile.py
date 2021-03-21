class Pile:
    def __init__(self,maxMaPile):
        self.maxpile = maxMaPile    #maxpile la taile maximale de la pile
        self.contenu =[]            #contenu de la pile initialisée par tableau vide []

    def pileVide(self):
        if len(self.contenu)==  0   :
            return True
        else:
            False                
    
    
    def pilePlein(self):
        if len(self.contenu) == self.maxpile:
            return True
        else:
            return False




    def empiler(self,e):
                        #ajouter des elements au contenu jusq'a se 'on atteint la taille maximum
        if    self.pilePlein():
            print("désolée la liste est plein vous ne pouvez pas ajouter à la liste ")
        else: 
            self.contenu.append(e)
            



    def depiler(self):
        if self.pileVide():
            print("Impossible: Pile vide")
        else:
            self.contenu.pop(-1)


    def purger(self):
        while not self.pileVide():
            self.depiler()

    def sommet(self):
        if not self.pileVide():
            tmp = self.contenu [len(self.contenu)-1]
            self.depiler()
            return tmp
        else:
            print("impossible la pile est vide")

    def __str__(self):
        return str(self.contenu)

    def afficher(self):
        print(self)

mapile1 = Pile(5)

print(mapile1)
mapile1.empiler(10)
print(mapile1)
mapile1.empiler(20)
print(mapile1)

mapile1.empiler(11)
print(mapile1)
mapile1.empiler(0)
print(mapile1)
mapile1.empiler(19)
print(mapile1)
mapile1.empiler(18)
print(mapile1)
mapile1.empiler(15)
mapile1.afficher()

print("voila le sommet",mapile1.sommet())

mapile1.depiler()
print(mapile1)
mapile1.purger()
print(mapile1)
print("voila le sommet",mapile1.sommet())
mapile1.purger()
print(mapile1)
mapile1.depiler()
mapile1.afficher()



