#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "S3_Exo6.h"

int main(){
    T_PERSONNE joueur1;
    printf("Entrez le nom du joueur :");
    scanf("%s",&joueur1.nom);
    getchar();

    printf("Entrez le prenom du joueur :");
    scanf("%s",&joueur1.prenom);
    getchar();

    joueur1.score = 0;

    printf("Entrez la lettre correspondance au niveau du joueur: ");
    scanf("%c \n",&joueur1.niveau);
    getchar();

   

    
    printf("%s %s \t \t ",joueur1.prenom,joueur1.nom);
    printf("\n  Score : %d au niveau : %c",joueur1.score,joueur1.niveau);
}