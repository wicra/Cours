

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // Initialisation du générateur de nombres aléatoires avec une graine
    srand(time(0));
    // Générer un nombre aléatoire entre 0 et 1
    int d1 = rand() % 7;
    int d2 = rand()%7 ;
    int resultat = d1 + d2 ;
    printf("%d", resultat);
    // Vérifier le résultat et afficher "pile" ou "face"
    

}

