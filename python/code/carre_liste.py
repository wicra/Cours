

def print_carre(tab:list) -> int:
    """
    tab est une liste fait en tableau
    --------
    print_carre doit afficher le carre de chaque element de la liste

    
    """
    for i in tab:
        print(i**2)
        

def map_carre(tab):
    t=[]
    for e in tab:
        t.append(e**2)   
    return t
