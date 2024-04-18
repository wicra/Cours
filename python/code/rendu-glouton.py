
# EXERCICE 2
# Voici le code que vous devez compléter
# Votre code doit vérifier les 2 assertions suivantes

Pieces = [100,50,20,10,5,2,1]
def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution
    p = Pieces[i]
    if p <= arendre :
        solution.append(p)
        return rendu_glouton(arendre - p, solution, i)
    else :
        return rendu_glouton(arendre, solution, i+1)

print(rendu_glouton(68,[],0))

assert rendu_glouton(68,[],0) == [50, 10, 5, 2, 1], "50 + 10 + 5 + 2 + 1 = 68"
assert rendu_glouton(291,[],0) == [100, 100, 50, 20, 20, 1], "100 + 100 + 50 + 20 + 20 + 1 = 291"
