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
print(extremum_tableau(F))

