
from Pile import *

def calculer(a,b,op):
    print("a=",a)
    print("b=",b)
    print("op=",op)


    if  op == '+':
        return float (a) + float(b)
    elif op == '-':
        return float (a) - float(b)
    elif op == '*' or op == 'X'or op == 'x':
        return float (a) * float(b)
    elif op == '/'or op == ":":
        return float (a) / float(b)
    else:
        print("erreur sur l'operation")

def estOperation(op):
    
    if  op == '+' or op == '*' or op == '-' or op =='/' or op == ":" or op == 'x' or op == 'X':
        return True
    else:
        return False

def estNombre(calcul):
     
    if type(calcul) == int or type(calcul) == float:
        return True
    else:
        return False

def NPI(calcul):
    
    mapile = Pile(5)
    cal = calcul.split()
    
    for i in range(len(cal)):
         if not estOperation(cal[i]):
            mapile.empiler(cal[i])   
            mapile.afficher()    
         else :
            operande2 = mapile.sommet() 
            mapile.afficher()
            operande1 = mapile.sommet()
            mapile.afficher()
            resultat = calculer(operande1,operande2,cal[i])
            mapile.empiler(resultat)
            mapile.afficher()

      
    return  mapile.sommet()


        

print(estOperation('5'))
print(estOperation('+'))
print(estNombre('+'))
print(estNombre('10.5'))
print(estNombre(10))

calcul1 = "2 3 + 4 -"
calcul2 = "2.57 3.9999 +"
print(NPI(calcul1))
print(NPI(calcul2))






            
