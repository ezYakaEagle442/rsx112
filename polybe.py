# Credits: https://www.apprendre-en-ligne.net/crypto/python/polybe/polybe.py

# carre de Polybe

def ecrire(s):
    i=0
    long = len(s)
    while i<long:
        print(s[i],end="")
        if (i+1)%6 == 0 :
            print(end=" ")
        i += 1
    print()


def chiffrer(s):
    chiffre=""
    s = s.upper()
    for lettre in s:
        if lettre in alphabet:
            ligne = alphabet.index(lettre)//5 + 1
            col = alphabet.index(lettre) % 5 + 1
            chiffre += str(ligne) + str(col)
    return chiffre


def dechiffrer(s):
    s1 = list(s)
    dechiffre = ""
    for i in range(0,len(s),2):
        ligne = int(s1[i])
        col = int(s1[i+1])
        lettre = alphabet[((ligne-1)*5 + col)-1]
        dechiffre += lettre
    return dechiffre


# construction de la grille a partir d'une clef

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']   # pas de W

def clef_grille(clef):   # cree une clef de 25 lettres differentes a partir d'une clef quelconque
    clef = clef.upper()
    clef_valide=""
    for ch in clef:
        if ch not in clef_valide:
            clef_valide += ch
    if len(clef_valide)<25:
        for ch in alpha:
            if ch not in clef_valide:
                clef_valide += ch
    return clef_valide


# test

clef = input("Clef : ")
alphabet = clef_grille(clef)
print("Grille : ",alphabet) # ex: TOABCD EFGHIJ KLMNPQ RSUVXYZ
clair= input("Texte clair : ")
chiffre = chiffrer(clair)
print("Texte chiffrÃ© : ",end="")
ecrire(chiffre)
dechiffre = dechiffrer(chiffre)
print("Texte dÃ©chiffrÃ© : ",dechiffre)