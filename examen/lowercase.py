
def numlowercase(chaine):
    if (len(chaine ) == 0):
        return 0
    else :
        if chaine[0].islower():
            return 1 + numlowercase(chaine[1:len(chaine)])
        else :
            return numlowercase(chaine[1:len(chaine)])

# Test

print (numlowercase("test"))
print (numlowercase("TEST"))
print (numlowercase("Test"))
print (numlowercase("Test"))