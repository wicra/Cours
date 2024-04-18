
#include <stdio.h>  /* Importation d'un Bibliothèque de base du C pour utiliser ex:printf */
// Exercice 1
int main(){
    
    int ici;
     
    printf("Entrer un chiffre: ");
    scanf("%d", &ici);
    getchar();
    if (ici == 10)
    {
        printf("Moyen");
    }
    if (ici > 10)
    {
        printf("au dessus ");
    }
    else 
    {
        printf("En dessous");
    }
   

}