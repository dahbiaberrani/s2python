from Pile import*





#definir une fonction qui vérifier les bonne parenthèse avec la methode Pile 


def pile_parenthes(expression):
    maPile = Pile(9)

    for i in range(len(expression)):    
        if expression[i] == '[':   
            maPile.empiler(']')
        elif expression[i] == '(':
            maPile.empiler( ')' )
        tmp = maPile.sommet()
        if  expression[i] != tmp:
            maPile.empiler(tmp) 
    return maPile.pileVide()
  



# tester une bonne expression 
mon_expression = "[a+(b+c)]"  
print(pile_parenthes(mon_expression))
#teste d'une fause expression
mon_expression1 = "[a+(b+c)"
print(pile_parenthes(mon_expression1))