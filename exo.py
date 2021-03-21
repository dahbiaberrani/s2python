
class Date:
    

    def __init__(self,j,m,a):
        self.jour = j
        self.mois = m
        self.annee = a 


    def anterieure(self, d):
        if d.annee < self.annee:
            return True
        elif d.annee == self.annee:
            if d.mois < self.mois:
                return True
            elif d.mois == self.mois:
                if d.jour < self.jour:
                    return True
        return False


    def Affecter(self):
        j = input("Entrez un jour : ")
        self.jour = int(j)
        self.mois = input("Entrez un mois : ")
        a = input("Entrez une annee : ")
        self.annee = int(a)


    def afficher(self):
        return str(self.jour) +"/"   + str(self.mois) +"/" + str(self.annee)

d1 = Date(7,3,2021)
print(d1.afficher())

# test de la Methode Anterieur

d2 = Date(7,4,2021)
print(d2.anterieure(d1))