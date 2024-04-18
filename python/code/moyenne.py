
# EXERCICE 1
# Ecrire ici votre code pour l'exercice 1
# Votre code doit vérifier les 3 assertions suivantes

def moyenne(t):
    if len(t) !=0:
        s=0
        for i in range(len(t)):
            s=s+t[i]
        return round(s/len(t),2)
    return "le tableau est vide"
print(moyenne([223,234,2345]))

assert moyenne([5,3,8]) == 16/3, "Erreur de calcul" # Réponse attendue : 5.333333333333
assert moyenne([1,2,3,4,5,6,7,8,9,10]) == 5.5, "Erreur de calcul" 
assert moyenne([]) == "erreur", "Le tableau est vide"
