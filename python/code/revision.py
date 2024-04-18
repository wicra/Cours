#HAZARD


def hazard(n):
    H=[]
    for u in range(n):
        r=randint(1,999)
        H.append(r)
    return H
#print(hazard(20))

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
#print(tri_selection(H))

#TRI PAR INSERSION 


I=[4,5,3,2,1]
def tri_insersion(I):           
    n=len(I)                            #1
    for i in range(1,n):                #1
        temp=I[i]                       #1
        j=i-1                           #2
        while j >= 0 and I[j]>temp:     #2
            I[j+1]=I[j]                 #2
            j=j-1                       #2
        
        I[j+1]=temp                     #2
    return I                            #1





#CHERCHER UN NOMBRE DANS UN TABLEAU

t=[3,11,5,7,101]

def recherche_tableau(x,t):
    for k in range(len(t)):
        if t[k]==x:
            return True
    return False
#print(recherche_tableau(5,t))




#CHERCHER LA REPETITION DANS UN TABLEAU

T=[3,11,5,7,5,101,5]

def occurences_tableau(x,T):
    R=[]
    for a in range(len(T)):
        if T[a]==x:
            R.append(a)            
    return R
    
    
#print(occurences_tableau(5,T))
#print(occurences_tableau(102,T))
#print(occurences_tableau(101,T))  




#LES MAX ET LE MIN D'UN TABLEAU

G=[11,1001,2,157,38]

def maxe_tableau(G):
    max=G[0]
    for k in range(1,len(G)):
        if max<G[k]:
            max=G[k]
    return max

def min_tableau(G):
    min=G[0]
    for i in range(1,len(G)):
        if min>G[i]:
            min=G[i]
    return min

#print(maxe_tableau(G))
#print(min_tableau(G))


#CHERCHER LE EXTREMUM MIN ET LE MAX EN MEME TEMPS

F=[11,1001,2,157,38]
MIN_MAX=[]

def extremum_tableau(F):
    max=F[0]
    min=F[0]
    for l in range(1,len(F)):
        if max<F[l]:
            max=F[l]
            MIN_MAX.append(max)
        elif min>F[l]:
            min=F[l]
            MIN_MAX.append(min)
    return MIN_MAX
#print(extremum_tableau(F))


def moyenne(notes):
    somme = 0
    somme_coeff = 0
    for couple in notes:
        somme += couple[1] * couple[0]
        somme_coeff += couple[1]
        return somme / somme_coeff
    

def conv_bin(n):
    b = []
    bit = 0
    while n != 0:
        bit += 1
        b.append(n % 2)
        n = n // 2
    b.reverse()
    return b, bit


def recherche_dichotomique(tab, n):
    deb = 0
    fin = len(tab) - 1
    mil = (fin + deb) // 2
    while deb <= fin:
        if tab[mil] == n:
            return mil
        elif tab[mil] < n:
            deb = mil + 1
        else:
            fin = mil - 1
        mil = (fin + deb) // 2
    return -1
