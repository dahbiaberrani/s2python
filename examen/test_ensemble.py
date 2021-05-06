
from Ensemble import * 

# tests
e1 = Ensemble()
print(e1.estVide())
print(e1.taille())
e1.ajouter(5)
print(e1.estVide())
print(e1.taille())
print(e1.estVide())
print(e1.present(5))
print(e1.present(410))
e1.ajouter(14)
print(e1.estVide())
print(e1.taille())
print(e1.at_index(0))
print(e1.at_index(1))
print(e1.at_index(2))
print(e1.at_index(-1))
print(e1)
e1.retirer(5)
print(e1)