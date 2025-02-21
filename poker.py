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


# https://docs.python.org/fr/3/library/random.html ,   
# /!\ Avertissement  Les générateurs pseudo-aléatoires de ce module ne doivent pas être utilisés à des fins de sécurité. 
# Pour des utilisations de sécurité ou cryptographiques, voir le module secrets. 
import secrets

# https://home.unicode.org/

# https://fr.windows-office.net/?p=14838
# /!\ Les codes Alt sont la combinaison de la touche Alt et des touches numériques du pavé numérique.
# /!\ You must use the numeric keypad to type the numbers, and not the keyboard. 

# Pour saisir un caractère Unicode au clavier :
# - Sous GNOME (Linux) : Ctrl+Shi􀅌+U (« u » apparaît à l’écran), puis le code hexadécimal, et valider avec Entrée
# - Sous Windows : maintenir la touche Alt enfoncée et saisir le code décimal, puis relâcher la touche Alt.
# https://support.microsoft.com/en-us/office/insert-ascii-or-unicode-latin-based-symbols-and-characters-d13f58d3-7bcb-44a7-a4d5-972ee12e50e0

# Symbole | Code hexadécimal | Code décimal
# ♠       | 2660             | 9824
# ♥       | 2663             | 9827
# ♦       | 2665             | 9829
# ♣       | 2666             | 9830

# Générer un jeu de 52 cartes
# Vous pouvez utiliser V(alet), D(ame), R(oi) au lieu de J(ack), Q(ueen) et K(ing) si vous le souhaitez.
suits = ['♠', '♥', '♦', '♣'] # couleurs
ranks = [str(n) for n in range(2, 11)] + list("JQKA") # valeurs
deck = [f"{rank}{suit}" for suit in suits for rank in ranks] # on crée le paquet de cartes, f"{rank}{suit}" indique "format string"

# Afficher le jeu
print(deck)

def getCard():

    # Dave Bayer and Persi Diaconis, Annals of Applied Probability 1992, Volume 2, n°2, p. 294-313
    # https://projecteuclid.org/euclid.aoap/1177005705
    # https://projecteuclid.org/journalArticle/Download?urlId=10.1214%2Faoap%2F1177005705 

    c=secrets.choice(deck)
    deck.remove(c)
    return c

# Distribuer 2 cartes à 5 joueurs
print("\n🔹 **Mains des joueurs:**")
for i in range (5):
    print("Joueur %i : %s  %s" % ( i+1, getCard(), getCard() ))

# Affichage de la table
print("\n🔹 **Cartes sur la table:**")
print("Table : %s  %s  %s  %s  %s" % ( getCard(), getCard(), getCard(), getCard(), getCard() ))