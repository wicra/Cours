#include <stdio.h>  /* Importation d'un Bibliothèque de base du C pour utiliser ex:printf */



// Exercice 4

int main(){

    int Ent1 ;
    scanf("%d",&Ent1);
    getchar();

    int Ent2;
    scanf("%d",&Ent2);
    getchar();

    int Ent3;
    scanf("%d",&Ent3);
    getchar();

    if (Ent1 > Ent2){
        if (Ent1 > Ent3){
            printf("Le Max%d ",Ent1);
        }
        else{
            printf("Le max%d",Ent3);
        }
        
    }
    
    else{
        printf("Le max%d",Ent2);
    }
    
}
