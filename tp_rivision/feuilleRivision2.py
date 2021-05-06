
# recherche max d'un liste

def maxRecursive(liste):
    if len(liste) ==0:
        return None
    if len(liste) ==1:
       return liste[0]
    a = maxRecursive(liste[1:])
    if liste[0] > a:
        return liste[0]
    else :
        return a




#exercice 2 divsion euclidienne
def eucli(a,b):
    if a < b:
        return a
    else:
        return eucli(a-b,b)



#exercie 
# creation d'un pile 
def creerPile():
    return []


def empiler(pile,elt):
    pile.append(elt)

def depiler(pile):
    if pileVide(pile):
        print("pile vide")
    else:
        pile.pop()

def pileVide(pile):
   return len(pile) == 0

def sommet(pile):
    return pile[-1]

def copiePile(pile):
    pile1 = creerPile()




def maccarthy(n):
    if n>100:
        return n-10
    else:
        return maccarthy(maccarthy(n+11))

# regarde si la liste est trie version 1
def estTrie(tab):
    if len(tab)<=1:
        return True
    else:
        return tab[0] <= tab[1] and estTrie(tab[1:])

# regarde si la liste est trie version 2
def estTrieVession2(tab):

    if len(tab)<=1:
        return True
    elif tab[0] > tab[1]:
        return False

    else:
        return estTrie(tab[1:])








liste1 = [2,3,5,8,14]
print(maxRecursive(liste1))
print(eucli(31,5))
pile1 = creerPile()
empiler(pile1,3)
empiler(pile1,30)
empiler(pile1,13)
empiler(pile1,40)
depiler(pile1)
print(pile1)

print(maccarthy(91))

liste1 = [2,3,5,8,14]
liste2 = [8,3,5,8,14]
print(estTrie(liste1))
print(estTrie(liste2))

print(estTrieVession2(liste1))
print(estTrieVession2(liste2))