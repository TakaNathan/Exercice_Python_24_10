#programme qui va mettre les espaces entre les
#lettres voisines

#fonction qui va prendre une chaine de caractere
#et retourne un autre caractere avec les espaces
#(str)-> str
def espaces(s) :
    s = s.replace(""," ")
    s = s.strip()
    return s

print(espaces("important"))