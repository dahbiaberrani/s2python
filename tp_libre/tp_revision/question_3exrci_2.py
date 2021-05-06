def parenthese_rec(expression):
    if len(expression) == 0:
        return True
    elif len(expression) == 1:
        return False
    else:
        return parenthese_rec(expression[0]) == parenthese_rec(expression[len(expression)-1]) and parenthese_rec(expression[1:len(expression)-2])





mon_expression = "[()]"  
mon_expression1 = "[()"

print(parenthese_rec(mon_expression))
print(parenthese_rec(mon_expression1))