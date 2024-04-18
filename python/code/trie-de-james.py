def trie(a, b):
    tab = []
    while a and b:  # Tant que les deux listes ne sont pas vides
        if a[0] > b[0]:
            tab.append(b[0])
            del b[0]
        else:
            tab.append(a[0])
            del a[0]
    # Ajouter les éléments restants de la liste non vide
    tab.extend(a)
    tab.extend(b)
    return tab

a = [2, 6, 12]
b = [5, 9, 45]
print(trie(a, b))
