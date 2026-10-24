#Fonction qui va recuperer une chaine de 
#caractere et retourner une nouvelle chaine 
#avec les paires de caractere inversees
#(str)->str
def coder(s) :
    reverse_s = ""
    i=0
    while i < len(s) :
        if i == len(s)-1 :
            reverse_s += s[i]
            break
        reverse_s += s[i+1]+s[i]
        i += 2
    return reverse_s

print(coder("message secret"))
print(coder("Message"))