/* SEANCE II 
Exercice 4 */

#include <stdio.h>  /* Importation d'un Bibliothèque de base du C pour utiliser ex:printf */

int main() {
    char prenom[20] = "wicra";      /* Char = charactere , [20] pour 20 char max */
    int tab[10] = {1,45,3,5,7,9,2,6,0,1}; /* Tableau de 10 entier */

    /* pour recuperer une valeur dans un tab il faut definir sa nature (%d) puis l'appeler avec Tab[un nombre]*/
    printf("1er element du tableau est = %d\n 2e element du tableau est = %d\n 3er element du tableau est = %d\n\n\n",tab[0],tab[1],tab[2]);    
    printf("Le code ASCII de:\n \tW =%d \n\tI =%d \n\tC =%d \n\tR =%d \n\tA =%d ",prenom[0],prenom[1],prenom[2],prenom[3],prenom[4]);
     /* il affiche le code ASCII grace a %d */
    printf("\nJe m'appelle :\n \tW =%c \n\tI =%c \n\tC =%c \n\tR =%c \n\tA =%c ",prenom[0],prenom[1],prenom[2],prenom[3],prenom[4]);
    return 0; /*juste pour verifier que tout est ok*/
}