# EXERCICE 1
# Ecrire ici votre code pour l'exercice 1
# Votre code doit vérifier les 3 assertions suivantes

def recherche(caractere, mot):
    compteur = 0
    for c in mot:
        if c == caractere:
            compteur = compteur + 1
    return compteur 

print(recherche("e","pepe"))
assert recherche('e', "sciences") == 2, "e apparait 2 fois dans le mot"
assert recherche('i',"mississippi") == 4, "i apparait 4 fois dans le mot"
assert recherche('a',"mississippi") == 0, "Il n'y a pas de a dans le mot !"
