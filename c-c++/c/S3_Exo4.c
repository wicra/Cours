#include <stdio.h>
#include <stdlib.h>


int main()
{
 
    char caractere;
    int valeur_Entier;
    float valeur_reel;
    char chaine[20];

    printf(" veuilleur saisir un caractère :");
    scanf("%c",&caractere);
    getchar();

    printf(" veuilleur saisir une valeur entier :");
    scanf("%d",&valeur_Entier);
    getchar();

    printf(" veuilleur saisir une valeur réel : ");
    scanf("%f",&valeur_reel);
    getchar();

    printf(" veuilleur saisir une chaine : ");
    scanf("%s",chaine);
    getchar();

    printf(" caractere : %c - valeur Entier : %d - veleur reel : %f - chaine : %s",caractere, valeur_Entier, valeur_reel, chaine);
}