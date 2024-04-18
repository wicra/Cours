# Module sur les nombres de Fibonacci
def fib(n:int)-> None:    # affiche les nombres de Fibonacci jusqu'à n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n:int)-> list:   # renvoie la liste des nombres de Fibonacci jusqu'à n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result






""" Module fibo relatif à la création de nombres de Fibionacci
Pour rappel, la suite de Fibonacci est une suite d'entiers dans laquelle chaque terme est la somme 
des deux termes qui le précèdent.(voir: https://fr.wikipedia.org/wiki/Suite_de_Fibonacci)


Ce module présente deux fonctions:


- fib_print: affiche les nombres de Fibionacci
- fib_to_array: renvoie la liste des nombres de Fibionacci


"""


def fib_print(n:int)-> int:
    """Affiche les nombres de Fibionacci


    Arguments
    ---------
    n: int
        dernier rang de la suite de Fibonacci affiché
        """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib_to_array(n:int)-> list:
    """Renvoie la liste des nombres de Fibionacci


    Arguments
    ---------
    n: int
        dernier rang de la suite de Fibonacci renvoyé dans la liste
    
    Returns
    -------
    list
        La liste des nombres de Fibionnaci jusqu'au rang n
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result



