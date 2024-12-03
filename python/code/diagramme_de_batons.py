import matplotlib.pyplot as plt

# Retourne la liste des lettres de l'alphabet
def alphabets():
    return [chr(i) for i in range(97,123)]

print(alphabets())

# # Calcule la factorielle d'un nombre n (n!)
# def factorielle(n):
#     Resu = 1
#     for i in range(1, n+1):
#         Resu *= i
#     return Resu
# 
# print(factorielle(3))

# Compte le nombre d'occurrences d'une lettre dans un texte
def frequenceLettre(lettre,texte):
    n = 0
    for i in texte:
        if i == lettre :
            n += 1
    return n
    
print(frequenceLettre("a","va bien manger un tajine"), "\n")

# Compte la fréquence de chaque lettre de l'alphabet dans un texte
def listeFrequences(texte):
    dico = {i:0 for i in alphabets()}
    for i in texte:
        if i in dico:
            dico[i] += 1
    return dico

texte = "va bien manger un tajine avec des fruits et des legumes et beaucoup de viande"
resultats = listeFrequences(texte)
print(resultats, "\n")

# Dessine un diagramme en batons des fréquences de chaque lettre de l'alphabet dans un texte
ep = 0.5
lettres = alphabets()
frequences = [resultats[lettre] for lettre in lettres]
plt.bar(lettres, frequences, ep, color='b')
plt.xlabel("Lettres")
plt.ylabel("Fréquences")
plt.title("Fréquences d'apparition des lettres dans le texte")
plt.show()