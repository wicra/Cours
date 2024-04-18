
from random import*
def premier(n) :
    x = randint (2,10)
    for k in range (2,523):             # en allant de 1 a 523
        if n % x == 1:                  # si le reste de n / 2 = 1
            simulation = 'oui'          # donc le nombre est pemier
        else :                          # si non
            simulation = 'non'          # le nombre n'est pas un nombre premier
    return (simulation)

print(premier(4))