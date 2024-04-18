#include <stdio.h>  /* Importation d'un Bibliothèque de base du C pour utiliser ex:printf */


//Exercice 6

int main(){
    int valeur;
    scanf("%d",&valeur);
    getchar();
    if (valeur % 2 != 0 || valeur % valeur != 0){
        printf("la valeur est paire");
    }
    else{
        printf("la valeur est impaire");
    }
    /*
    while (i>20){
        printf("la valeur est impaire");


    }
    */


}
