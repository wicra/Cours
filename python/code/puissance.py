#PUISSANCE IMPERATIVE
def puissance(n):
    a=1
    for k in range(n):
        a=a*2
    return a

print(puissance(0))
print(puissance(8))

#PUISSANCE RECURSSIVE
def puissance_rec(n):
    if n == 0:
        return 1
    else:
        return 2 * puissance_rec(n-1) 
print(puissance_rec(4))

#FACTORIELLE
def factorielle(n):
    cmp =1
    for i in range(2,n+1):
        cmp=cmp*i
    return cmp
print(factorielle(6))

#FACTORIELLE RECCURCIVE
def factorielle_rec(n):
    if n == 0:                  # <- cas de base
        return 1
    else:                       # <- recursif
        return n *factorielle_rec(n-1) 
print(factorielle_rec(5))

#QUITE FIBO
def fibo(n):
    u0=0
    u1=1
    for i in range(n):
        u0=u0+u1
        print(u0)
        u1=u1+u0
        print(u1)
    return u1
print(fibo(3))
