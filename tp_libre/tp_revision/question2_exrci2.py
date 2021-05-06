from Pile import*


def estexpression(op):
    if op ==  '('  or op == ')':
        return True
    else:
        return False



def return_parenthes(expression):
    maPile1 = Pile(9)

    for i in range(len(expression)):
        #print(expression[i]) 
        if estexpression(expression[i]) :   
            maPile1.empiler(expression[i])
            
    return maPile1.toString()


expression1 = "((a*3)+(2*b))/2"
print(return_parenthes(expression1))
expression2 = "((a+b) * c)"
print(return_parenthes(expression2))