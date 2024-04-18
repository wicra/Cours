# EXERCICE 2
# Voici le code que vous devez compléter
# Votre code doit vérifier les 2 assertions suivantes

def tri(tab):
    #i est le premier indice de la zone non triee, j le dernier indice. 
    #Au debut, la zone non triee est le tableau entier.
    i= 0
    j= len(tab)-1
    while i != j :
        if tab[i]== 0:
            i= i+1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i]= valeur
            j= j-1
    return tab

print(tri([0,1,0,1,0,1,0,1,0]))

assert tri([0,1,0,1,0,1,0,1,0]) == [0, 0, 0, 0, 0, 1, 1, 1, 1]
assert tri([0,1,0,1,0,0,0,1,0,1,1,1,0,1,0,1,1]) == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]




###########      UN AUTRE EXEMPLE     ##########
from random import randint
#HAZARD
H=[]
def hazard(n):
    for u in range(n):
        r=randint(1,999)
        H.append(r)
    return H

#TRI PAR SELECTION 
def tri_selection(H):                   
    for k in range(len(H)-1):           #1     
        min=H[k]                        #1
        imin=k                          #1
        for i in range(k+1,len(H)):     #1
            if H[i]<min:                #1
                min=H[i]                #1
                imin=i                  #1
        temp=H[k]                       #1
        H[k]=H[imin]                    #1  
        H[imin]=temp                    #1
    return H                            #1
print(tri_selection(H))

