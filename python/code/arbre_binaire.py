# nécessaire pour pouvoir annoter le type de la classe
from __future__ import annotations

class ArbreBinaire:
    """Structure de donnée d'arbre binaire"""
    def __init__(self, étiquette: str, gauche: ArbreBinaire, droit: ArbreBinaire):
        self.étiquette = étiquette
        self.gauche = gauche
        self.droit = droit

def taille(arbre):
    if arbre is None:
        return 0
    else:
        return 1+taille(arbre.gauche)+taille(arbre.droit)
        
def hauteur(arbre):
    if arbre is None:
        return 0
    else:
        return 1+max(hauteur(arbre.gauche),hauteur(arbre.droit))

#Arbre binaire
ArbreBinaire("F",ArbreBinaire("B",ArbreBinaire("A",None,None),ArbreBinaire("D",ArbreBinaire
("C",None,None),ArbreBinaire("E",None,None)))
,ArbreBinaire("G",None,ArbreBinaire("I",ArbreBinaire("H",None,None),None)))

#exemple d'arbre binaire
ArbreBinaire(12,ArbreBinaire(3,ArbreBinaire(4,None,None,ArbreBinaire(11,None,None))),ArbreBinaire(25,None,None),
ArbreBinaire(22,ArbreBinaire(15),None,None),ArbreBinaire(31,ArbreBinaire(36,None,None),ArbreBinaire(57,None,None)))

