#CHERCHER UN NOMBRE DANS UN TABLEAU

t=[3,11,5,7,101]

def recherche_tableau(x,t):
    for k in range(len(t)):
        if t[k]==x:
            return True
    return False
print(recherche_tableau(5,t))

