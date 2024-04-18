
tab =[2,5,6,2]
fini = []
def bulle(tab):
    permut = 0
    temp = 0
    for i in range(len(tab)):
        if tab[i]>tab[i+1]:
            permut = tab[i]
            temp=tab[i+1]
            
        print(tab[i])

    print(tab)
            
bulle([2,5,6,2])
"""

    while permut == True:
        permut = False
        passage_dans_cet_ietration = 0
        for i in range (1,tab-1):
            if tab[i] > tab[i+1]:
                permut= True
                passage_dans_cet_ietration += 1
        passages +=1
    return passages
"""