# EXERCICE 1

def recherche(elt,tab):
    indice = 0
    for f in tab:
        if f == elt:
            return indice
        indice = indice + 1
    return -1

print(recherche(1,[2,3,4]))
'''
assert recherche(1, [2, 3, 4]) == -1 , "L'élément 1 n'est pas dans tab."
assert recherche(1, [10, 12, 1, 56]) == 2, "L'élément 1 est dans tab à l'indice 2."
assert recherche(50, [1, 50, 1]) == 1, "L'élément 50 est dans tab à l'indice 1."
assert recherche(15, [8, 9, 10, 15]) == 3, "L'élément 15 est dans tab à l'indice 3."
'''