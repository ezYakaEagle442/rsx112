# Credit: https://www.apprendre-en-ligne.net/crypto/python/playfair/playfair.py

from random import choice

##### Définition des classes : #####


class Grille:
    def __init__(self, clef):
        self.creer(clef)

    def creer(self, clef):
        "Composition d'une grille chiffrante a partir d'une clef de 25 caracteres"
        k=0
        self.grille = []                                                                            # Création d'une nouvelle grille.
        for i in range(5):                                                                          # Ajout de 5 lignes.
            ligne = []                                                                              # Création d'une nouvelle ligne (vide).
            for j in range(5):                                                                      # Ajout de 5 lettres dans la ligne.
                ligne.append(clef[k])
                k+=1
            self.grille.append(ligne)

    def ecrire(self):
        for i in range(5):
            for j in range(5):
                print(self.grille[i][j],end=" ")
            print()

    def playfair_chiffrer(self, texte):
        "Chiffrement des bigrammes du [texte] chiffré avec la [grille] de chiffrement."
        coord = self.remplacer_coordonnees(texte)
        texte_clair = ''
        l = 0
        while(l < len(texte)):
            if(coord[l][0] == coord[l+1][0]):                                           # Si sur même ligne :
                texte_clair += self.grille[coord[l][0]][(coord[l][1]+1)%5]
                texte_clair += self.grille[coord[l+1][0]][(coord[l+1][1]+1)%5]
            elif(coord[l][1] == coord[l+1][1]):                                         # Si dans même colonne :
                texte_clair += self.grille[(coord[l][0]+1)%5][coord[l][1]]
                texte_clair += self.grille[(coord[l+1][0]+1)%5][coord[l+1][1]]
            else:                                                                                   # Sinon :
                texte_clair += self.grille[coord[l][0]][coord[l+1][1]]
                texte_clair += self.grille[coord[l+1][0]][coord[l][1]]
            l += 2
        return texte_clair

    def playfair_dechiffrer(self, texte):
        "Déchiffrement des bigrammes du [texte] chiffré avec la [grille] de chiffrement."
        coord = self.remplacer_coordonnees(texte)
        texte_clair = ''
        l = 0
        while(l < len(texte)):
            if(coord[l][0] == coord[l+1][0]):                                           # Si sur même ligne :
                texte_clair += self.grille[coord[l][0]][(coord[l][1]-1)%5]
                texte_clair += self.grille[coord[l+1][0]][(coord[l+1][1]-1)%5]
            elif(coord[l][1] == coord[l+1][1]):                                         # Si dans même colonne :
                texte_clair += self.grille[(coord[l][0]-1)%5][coord[l][1]]
                texte_clair += self.grille[(coord[l+1][0]-1)%5][coord[l+1][1]]
            else:                                                                                   # Sinon :
                texte_clair += self.grille[coord[l][0]][coord[l+1][1]]
                texte_clair += self.grille[coord[l+1][0]][coord[l][1]]
            l += 2
        return texte_clair

    def remplacer_coordonnees(self, texte):
        "Remplacement de chaque lettre du message codé par ses coordonnées dans la grille : [[ligne_lettre0, colonne_lettre0] , [ligne_lettre1, colonne_lettre1], ...]."
        coord = []
        for l in range(len(texte)):
            groupe = []
            for i in range(5):                                                                      # Recherche des "coordonnées" de la l-ième lettre du texte.
                for j in range(5):
                    if(texte[l] == self.grille[i][j]):
                        groupe.append(i)
                        groupe.append(j)
            coord.append(groupe)
        return coord


# clef


def clef_grille(clef):   # cree une clef de 25 lettres differentes a partir d'une clef quelconque
    clef=clef.upper()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    clef_valide=""
    for ch in clef:
        if ch not in clef_valide and ch in alphabet:
            clef_valide += ch
    for ch in alphabet:
        if ch not in clef_valide:
            clef_valide += ch
    return clef_valide


def clair_conforme(clair):  # remplace les W par des V et insère un X entre deux lettres identiques
    clair = clair.upper()
    conforme = ""
    i = 0
    longueur = len(clair)
    while i < longueur:
        a = clair[i]
        if a == "W":
            a = "V"
        if i == longueur-1:   # ajoute une lettre aleatoire si la longueur du clair est impaire
            b = choice(['G', 'H', 'K', 'Y', 'Z'])
        else:
            b = clair[i+1]
            if b == "W":
                b = "V"

        if a == b : # insere un X entre deux lettres identiques
            b = "X"
            i += 1
        else:
            i += 2

        conforme += a
        conforme += b
    return conforme




# programme principal

clef = clef_grille("madamebovary")
grille = Grille(clef)
grille.ecrire()

clair = "NOUSETIONSALETUDEQUANDLEPROVISEURENTRASUIVIDUNNOUVEAUHABILLEENBOURGEOISETDUNGARCONDECLASSEQUIPORTAITUNGRANDPUPITRECEUXQUIDORMAIENTSEREVEILLERENTETCHACUNSELEVACOMMESURPRISDANSSONTRAVAIL"
print("clair")
print(clair)
conforme = clair_conforme(clair)
print("conforme")
print(conforme)
chiffre = grille.playfair_chiffrer(conforme)
print("chiffré")
print(chiffre)
dechiffre = grille.playfair_dechiffrer(chiffre)
print("déchiffré")
print(dechiffre)


