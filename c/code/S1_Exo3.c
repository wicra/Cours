/* SEANCE II 
Exercice 3 */
#include <stdio.h>  /* Importation d'un Bibliothèque de base du C pour utiliser ex:printf */

int main() {
    char prenom[20] = "wicra";      /* Char = charactere , [20] pour 20 char max */
    char nom[20]= "sergio";         
    int age = 19;                   /* Int = entier */
    char lycee[20] = "Baggio";

    /* %s = pour definir que c'est un Char avec limitaion , %d = int(-32mile a 32milz) ,%ld = long int (miliard), %u = unsigned int (0 a 60 mile), %f = float , %c = char (1 caratère) */
    printf(" prenom = %s\n nom = %s\n age = %d\n lycee = %s\n", prenom,nom,age,lycee);
    return 0;
}

