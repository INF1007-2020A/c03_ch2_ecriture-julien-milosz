#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    for lettre in mot:
        # TODO completer la fonction ici
        if ord(lettre)<=122 or ord(lettre)>=97:
            lettre = chr(ord(lettre)-32) # enlever 32 au code décimal de chaque lettre si elle est majuscule
        resultat += lettre
    return resultat


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
