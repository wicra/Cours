class carte :
    def __init__(self,valeur, couleur):
        self.valeur = valeur 
        self.couleur = couleur

    def getAttributs(self):         #GETTER (permet de recupere la valeur)
        return (self.valeur , self.couleur)

    def getValeur(self):            #GETTER
        return self.valeur                    #pas besoin de () car c'est deja un Tuple

    def getCouleur(self):           #GETTER
        return self.couleur


    def SetValeur(self , v):            #SETTER (pour verifier et modifier la valeur)
        if 1 <= v <= 13:                # v doit etre entre 1 et 13
            self.valeur = v
            return True
        else :
            return False

    def SetCouleur(self , c):
        #if c == 'trefle' or 'coeur' or 'pique' or 'careau':
        self.couleur = c
            #return True
        #else:
            #return False


cart1=carte(7,'trefle')
cart2=carte(3,'coeur')  
cart3=carte(13,'coeur')

print(cart1.valeur)
print(cart1.couleur)

print(f" {cart2.valeur} {cart2.couleur}")  # facon d'afficher les deux en une seul ligne 

print(cart1.getAttributs())             # affiche les deux attribut 

print(cart1.getCouleur())               # affiche que la couleur
print(cart1.getValeur())                # affiche que la valeur 

print(cart1.SetValeur(10))              # pour modifier la valeur si il est compris entre 1 et 13
print(cart1.SetValeur(15))              # la valeur depasse 13 
print(cart1.getValeur())

print(cart2.SetCouleur('pique'))        # ahhh non la cart 2 n'est pas un Coeur mais un pique 
print(cart2.getCouleur())   


print(cart3.getAttributs())             #  montre c'est quoi la cart 3
print(cart3.SetValeur(12))              # ahhh nonn enfait ma cart n'est pas un roi mais une dame
print(cart3.getAttributs())             # montre c'est quoi la cart 3
print(cart3.SetCouleur('pique'))        # ahhh nonn enfait ma cart n'est pas un coeur mais un pique 
print(cart3.getAttributs()) 
print(cart3.SetValeur(1))               # ahhh nonn enfait ma cart n'est pas une dame mais un A
print(cart3.getAttributs())



