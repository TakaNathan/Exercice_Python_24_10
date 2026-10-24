
s = ''' En 1815, M. Charles-François-Bienvenu Myriel était évêque de\n
Digne. C’était un vieillard d’environ soixante-quinze ans ; il occupait le\n
siège de Digne depuis 1806. … '''

#(a) Créez une copie de s, nommé nS, avec les caractères . , ; et \n remplacées par des espaces.
nS = s.replace("."," ")
nS = nS.replace(","," ")
nS = nS.replace(";"," ")
nS = nS.replace("\n"," ")
print(nS)

#(b) Effacez les espaces qui sont au début ou a la fin de nS (et affectez le nouveau chaine a la même variable nS). 
nS = nS.strip()
print(nS)

#(c) Changez tous les caractères de nS en minuscules (et nomme zle nouveau chaine nS).
zle = nS.lower()
print(zle)

#(d) Calculez le nombre des fois nS contient 'de'. 
n = nS.count("de")
print("Nombre de \'de\' est :",n)

#(e) Changez tous les sous-chaine était a est (et nommez le nouveau chaine nS).
nS = nS.replace("était","est")
print(nS)