#Programme qui va compter le nbre d'occurences
#d'un caractere dans une chaine de caractere

#fonction qui compte en utilisant count
#(str,str)-> int
def compte_count(string,caractere) :
    nombre = string.count(caractere)
    return nombre

#fonction qui compte avec les boucles
def compte_boucle(string,caractere) :
    nombre = 0
    for i in range(len(string)) :
        if string[i] == caractere[0] :
            for j in range(len(caractere)):
                if string[i+j] != caractere[j]:
                    continue
                elif j == len(caractere)-1 :
                    nombre +=1
    return nombre

s = input(" Entrer la chaine de caractère\n")
nombre_a = compte_count(s,'a')
nombre_de_la = compte_count(s,'de la')
print("Nombres d'occurences de \'a\'",nombre_a)
print("Nombres d'occurences de \'de la\'",nombre_de_la)
#Avec les boucles
print("#########")
nombre_a = compte_boucle(s,'a')
nombre_de_la = compte_boucle(s,'de la')
print("Nombres d'occurences de \'a\'",nombre_a)
print("Nombres d'occurences de \'de la\'",nombre_de_la)

                