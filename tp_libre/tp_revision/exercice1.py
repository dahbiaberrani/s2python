
#definir une fonction qui vérifier les bonne parenthèse avec Récursive


list = []
def FizzBuzz(d,n):
    
    if n < d:
        print(list)
    elif d % 3 == 0 and d % 5 == 0:
        list.append("FizzBuzz")
        FizzBuzz(d+1,n)
    elif d % 3 == 0: 
        list.append("Fizz")
        FizzBuzz(d+1,n)
    elif d % 5 == 0:
        list.append("Buzz")
        FizzBuzz(d+1,n)
    else:
        list.append(d) 
        FizzBuzz(d+1,n)
     

FizzBuzz(1,9)
