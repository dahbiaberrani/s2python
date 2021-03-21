# dahbia Berrani 

def factoriel(n):
    if n == 0 or n == 1 :
        return 1 
    else:
        return n*factoriel(n-1)


def sommeCarre(n):
    
    if   n == 0 :
        return 0

    else:
        return n**2 + sommeCarre(n-1)
    


def SommeTableau(tableau,indice=0):
    
    if indice == len(tableau) :
        return 0 

    else:
        if tableau[indice] > 0:

            return tableau[indice] + SommeTableau(tableau,indice+1)
        else:
            return SommeTableau(tableau,indice+1)

#def tableauIverser(tableau):
 #   if len(tableau)== 0 :
  #      return []
   # else:
    #    return tableauIverser(tableau[1:len(tableau)]) + [tableau[0]]


def tableauInverser(tableau,indice):

    if indice <len(tableau)/2:
        tmp = tableau[indice]
        tableau[indice] =tableau[len(tableau)-indice-1]
        tableau[len(tableau)-indice-1] = tmp
        tableauInverser(tableau,indice+1)

        return tableau


def palindrome(mots,indice):

    if indice >len(mots)/2:
        return True
    else:
         return mots[indice] == mots[len(mots)-1-indice] and palindrome(mots,indice+1)
   
    
def FibonacciRecursi(n):
    if n < 0 :
        return "erreur"
    elif n <= 1:
        return n
    else:
        return FibonacciRecursi(n-1) + FibonacciRecursi(n-2)

def FibonIterative(n):
    if n <= 1:
        return n
    else:
        moins2 = 0
        moins1 = 1
        for i in range(0,n):
            Un = moins2 + moins1
            moins1 = moins2
            moins2 = Un
    return moins2 + moins1


# La forme récursive est plus facile à écrire que la forme itérative 
tabble = [0,8,1,2,7,-9]
table = [1,2,3,4,5]

print(factoriel(5))
print(sommeCarre(5))
print(SommeTableau(tabble))
print(tableauInverser(table,0))
print(palindrome("kayak",0))
print(palindrome("coucou",0))
print(FibonacciRecursi(-1))
print(FibonacciRecursi(6))
print(FibonIterative(5))
print(FibonIterative(-1))
