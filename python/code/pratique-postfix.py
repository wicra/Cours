# Compléter le script
class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """
        Renvoie le booléen True si la pile est vide, False sinon.
        """
        return self.contenu == []
    
    def empiler(self, v):
        """Place l’élément v au sommet de la pile."""
        self.contenu.append(v)
        
    def depiler(self):
        """
        Retire et renvoie l’élément placé au sommet de la pile,
        si la pile n’est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()
 

def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' and element != '*':
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler()* p.depiler()
            p.empiler(resultat)
    return resultat

print(eval_expression([2, 3, '+', 5, '*']))


def max_dico(dico):
    vmax=0
    kmax=None
    for k in dico:
        if dico[k] > vmax :
            vmax=dico[k]
            kmax=k
        return(kmax ,vmax)        
        
max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50})