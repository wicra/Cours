
// Rentrer une Date
#include <stdio.h>

int main (){

    int jour;
    int mois;
    int annee;

    printf ("Veuillez saisir une date au format jj/mm/aaaa :");
    scanf("%d/%d/%d",&jour,&mois,&annee);
    getchar();
    printf ("Nous sommes le : %d-%d-%d\n", jour, mois, annee) ;

}

