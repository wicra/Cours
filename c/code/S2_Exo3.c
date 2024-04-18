#include <stdio.h>  /* Importation d'un Bibliothèque de base du C pour utiliser ex:printf */


//Exercice 3

int main(){

    int Car1 ;
    scanf("%d",&Car1);
    getchar();

    int Car2;
    scanf("%d",&Car2);
    getchar();

    if (Car1 > Car2){
        printf("%d %d",Car2,Car1);
    }
    else{
        printf("%d %d ",Car1,Car2);
    }
    
}

