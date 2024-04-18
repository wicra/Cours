from random import*

#CREE UN TABLEAU ALEATOIR
H=[]
def hazard(n):
    
    for u in range(n):
        r=randint(1,999)
        H.append(r)
    return H
print(hazard(20))


#SUP NOMBRE PAIRE
I=[]
def sup_pair(H):
    
    for k in H:
        if k%2 != 0 :
            I.append(k)
    return I

print(sup_pair(H))

#INSERER UN NOMBRE