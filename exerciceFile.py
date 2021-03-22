from File import*
taille_collier = 10
collier = File(taille_collier)
def remplir():
    for i in range(taille_collier-1):
         
        collier.ajouter("bleu")
    
def ajouter_milieu_collier():
    for i in range(taille_collier//2):
        
        tmp = collier.retirer()
        collier.ajouter(tmp)
    collier.ajouter("vert")
    for i in range((taille_collier//2)-1):
        tmp = collier.retirer()
        collier.ajouter(tmp)



remplir()
collier.afficher()
ajouter_milieu_collier()
collier.afficher()

