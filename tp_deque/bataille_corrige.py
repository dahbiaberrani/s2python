from collections import deque
 
#tableaux d'entiers à affecter aux mains des joueurs 1 et 2
donne1 = [10,13,6,10,8,14,12,3,7,13,9,2,11,13,3,2,12,14,11,7,13,10,4,14,5,5]
donne2 = [2,9,8,4,5,14,11,12,7,5,4,6,6,12,9,10,4,11,6,3,8,3,7,9,8,2]

    #initialisation de la partie
joueur1=deque(donne1)
joueur2=deque(donne2)
defausse1=deque()
defausse2=deque()

nbTours=0

    #affectation des cartes aux joueurs

while (len(joueur1)>0 and len(joueur2) >0):
 nbTours=nbTours+1
 
 j1=joueur1.popleft()
 j2=joueur2.popleft()
 
    #si la carte du j1 est > que celle de j2
if(j1 > j2):
    print("Joueur 1 remporte le tour")
    #ajout des cartes jouées aux defausses
    defausse1.append(j1)
    defausse2.append(j2)
    
    #le joueur1 recupere les cartes des defausses
    #les defausses sont videes
    while(len(defausse1)>0):
        joueur1.append(defausse1.popleft())
    while(len(defausse1)>0):
        joueur1.append(defausse2.popleft())
        
    print( joueur1)
    print( joueur2)

    #sinon si la carte de j2 est > a celle de j1
elif(j1 < j2):
    print("Joueur 2 remporte le tour")
    #ajout des cartes jouées aux defausses
    defausse1.append(j1)
    defausse2.append(j2)
            
    #le joueur2 recupere les cartes des defausses
    #les defausses sont videes
    while(len(defausse1)>0):
        joueur2.append(defausse1.popleft())
            
    while(len(defausse2)>0):
        joueur2.append(defausse2.popleft())
                
    print( joueur1 )
    print( joueur2 )

else:
    #bataille
    # on remet a gauche les cartes supprimés dans leurs deques joueur
    joueur1.appendleft(j1)
    joueur2.appendleft(j2)
    
    #ajout des cartes de bataille + 3 cartes aux defausses
    print("Bataille entre les deux joueurs !")
    
    for i in range(4):
        if len(joueur1) > 0:
            defausse1.append(joueur1.popleft())
 
    for i in range(4):
        if len(joueur2) > 0:
            defausse2.append(joueur2.popleft())
        
    print( joueur1 )
    print( joueur2)

 
print("Nombre de tours joues : {} ".format(nbTours))

if (len(joueur1)==0 and len(joueur2)>0):
    print("Joueur 2 gagne la partie")
elif(len(joueur2)==0 and len(joueur1) > 0):
    print("Joueur 1 gagne la partie")
 
 
 
 
 
 
 
 
 
 
 
