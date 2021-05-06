

from collections import deque



 




#tableaux d'entiers de taille 26 à affecter aux mains des joueurs 1 et 2
donne1 = [10,13,6,10,8,14,12,3,7,13,9,2,11,13,3,2,12,14,11,7,13,10,4,14,5,5]
donne2 = [2,9,8,4,5,14,11,12,7,5,4,6,6,12,9,10,4,11,6,3,8,3,7,9,8,2]

#initialisation de la partie
joueur1=deque(donne1)
joueur2=deque(donne2)
defausse1=deque()
defausse2=deque()

nbTours=0
#affectation des cartes aux joueurs
#tant que les joueurs ont des cartes
while (len(joueur1)>0 and len(joueur2) >0):
    nbTours=nbTours+1
    
    j1=joueur1.popleft()
    j2=joueur2.popleft()


    #combat gagne par j1
    if j1 > j2:
        defausse1.append(j2)
    #combat gagne par j2
    else :
        defausse2.append(j2)


        
#bataille
	
#affichage des resultats de la partie : joueur vainqueur et nombre de tours joués
