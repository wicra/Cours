
#LIFO (PILE = Empiler)

P=[]
def est_vide_P(P):
    n=len(P)
    if n==0:
        return True
    else:
        return False


def empiler(x):
    P.append(x)
    return P

def depiler(P):
    P.pop()
    return P

def sommet(P):
    return P[len(P)-1]

'''
print(est_vide_P(P)) 
print(empiler(17))
print(empiler(7))
print(empiler(20))
depiler(P)
print(empiler(13))
print(sommet(P))
print(est_vide_P(P))
'''

#FIFO (FILE)

def est_vide_F(P):
    n=len(P)
    if n==0:
        return True
    else:
        return False


def enfiler(x):
    P.append(x)
    return P

def defiler(P):
    P.pop(0)
    return P


def tete(P):
    return P[0]

'''
print(est_vide_F(P)) 
print(enfiler(17))
print(enfiler(7))
print(enfiler(20))
print(defiler(P))
print(enfiler(13))
print(tete(P))
print(est_vide_F(P))'''