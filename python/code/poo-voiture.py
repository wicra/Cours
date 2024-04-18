from matplotlib.pyplot import cla

class voiture :
    def __init__(self,couleur,kilometrage):
        self.couleur = couleur
        self.kilometrage = kilometrage
    
    def presentation(self):
        print(f"La voiture {self.couleur} a {self.kilometrage} kilometre ")


voiture1 = voiture("Bleu", 20000)
voiture2= voiture("Rouge",30000)

print(voiture1.presentation())
print(voiture2.presentation())

class personne :
    def __init__(self ,nom , annee_de_naissance ,lieu_naissance):
        self.nom = nom
        self.annee_de_naissance = annee_de_naissance
        self.lieu_naissance = lieu_naissance

    def __init__(self,titre,realisateur,personne):
        self.titre = titre
        self.realisateur = realisateur
        self.personne = personne

    def presentation_pers(self):
        print(f"le realisateur {self.nom} né {self.annee_de_naissance} {self.lieu_naissance}")
    
lautner = personne('Gorges lautner',1926,'nice')

print(lautner.presentation_pers())
        
        