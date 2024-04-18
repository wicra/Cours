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
