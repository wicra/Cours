from random import randint
#HAZARD
def hazard(n):
    H=[]
    for u in range(n):
        r=randint(1,999)
        H.append(r)
    return H

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

print(tri_insersion(I))

print('-------------------------------')
print('n=', 50)
tab = hazard(50)
print(tab)
print(tri_insersion(tab))
print('-------------------------------')
print('n=', 7)
tab = hazard(7)
print(tab)
print(tri_insersion(tab))
print('-------------------------------')
print('n=', 250)
tab = hazard(250)
print(tab)
print(tri_insersion(tab))