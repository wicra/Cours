

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // Initialisation du générateur de nombres aléatoires avec une graine
    srand(time(0));
    // Générer un nombre aléatoire entre 0 et 1
    int resultat = rand() % 7;

    // Vérifier le résultat et afficher "pile" ou "face"
    if (resultat != 0) {
        printf("%d",resultat);
    } 

    return 0;
}
