#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

# sudo apt install python3.12
# python3.12 --version
# sudo apt install python3-pip
# do NOT run : curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12
# pip3.12 -V

##########################################################################
#
# usage: python3 poker.py
#
##########################################################################

import random

# https://home.unicode.org/

# https://fr.windows-office.net/?p=14838
# /!\ Les codes Alt sont la combinaison de la touche Alt et des touches numériques du pavé numérique.
# /!\ You must use the numeric keypad to type the numbers, and not the keyboard. 

# Pour saisir un caractère Unicode au clavier :
# - Sous GNOME (Linux) : Ctrl+Shi􀅌+U (« u » apparaît à l’écran), puis le code hexadécimal, et valider avec Entrée
# - Sous Windows : maintenir la touche Alt enfoncée et saisir le code décimal, puis relâcher la touche Alt.
# https://support.microsoft.com/en-us/office/insert-ascii-or-unicode-latin-based-symbols-and-characters-d13f58d3-7bcb-44a7-a4d5-972ee12e50e0

# Symbole | Code hexadécimal |Code décimal
# ♠       | 2660             | 9824
# ♥       | 2663             | 9827
# ♦       | 2665             | 9829
# ♣       | 2666             | 9830

# Générer un jeu de 52 cartes
# Vous pouvez utiliser V(alet), D(ame), R(oi) au lieu de J(ack), Q(ueen) et K(ing) si vous le souhaitez.
suits = ['♠', '♥', '♦', '♣'] # couleurs
ranks = [str(n) for n in range(2, 11)] + list("JQKA") # valeurs
deck = [f"{rank}{suit}" for suit in suits for rank in ranks] # on crée le paquet de cartes, f"{rank}{suit}" indique "format string"

def riffle_shuffle(deck):
    half1, half2 = deck[:26], deck[26:]  # On effectue une 1ère coupe classque en divisant le paquet en deux
    # half1 contient les 26 premières cartes
    # half2 contient les 26 dernières cartes
    shuffled = [] # Cette liste va contenir le paquet après le mélange.

    # Dave Bayer and Persi Diaconis, Annals of Applied Probability 1992, Volume 2, n°2, p. 294-313
    # https://projecteuclid.org/euclid.aoap/1177005705
    # https://projecteuclid.org/journalArticle/Download?urlId=10.1214%2Faoap%2F1177005705 

    # Tant qu'il reste des cartes dans half1 ou half2, on continue le mélange.
    # random.random() génère un nombre entre 0 et 1.
    while half1 or half2:
        # On choisit aléatoirement une carte de half1 ou half2 :
        if half1 and (not half2 or random.random() < len(half1) / (len(half1) + len(half2))):
            # Si la condition est vraie, on prend une carte de half1 et on l'ajoute à shuffled
            # La méthode .pop() est utilisée pour extraire et retourner un élément d'une liste. 
            # Elle le supprime également de la liste d'origine, on a donc l'assurance qu'une carte ne sera pas sélectionnée deux fois.
            shuffled.append(half1.pop(0))
        else:
            # Sinon, on prend une carte de half2.
            shuffled.append(half2.pop(0))

    return shuffled

# On mélange 7 fois comme expliqué dans la vidéo de Bayer & Diaconis
for _ in range(7):
    deck = riffle_shuffle(deck)

# Afficher le jeu mélangé
# print(deck)

# Distribuer 2 cartes à 5 joueurs
hands = [deck[i:i+2] for i in range(0, 10, 2)]
table = deck[10:15]

print("\n🔹 **Mains des joueurs:**")
for i, hand in enumerate(hands, 1):
    print(f"Joueur {i}: {', '.join(hand)}")

# Affichage de la table
print("\n🔹 **Cartes sur la table:**")
print(", ".join(table))