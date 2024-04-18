#include <stdio.h>  /* Importation d'un Bibliothèque de base du C pour utiliser ex:printf */
#include<stdlib.h>



//Exercice 5


int main(){

    
    int Car2 ;
    int Car1 = 99 ;
 
    int compteur=0;

    while (Car1 != Car2){
        
        scanf("%d",&Car2);
        getchar();

        if (Car1 < Car2){
            printf("tu est trop grand \n essaie%d \n",compteur++);
        }
        if (Car2 < Car1){
            printf("tu est trop petit \n essaie%d \n",compteur++);
        }
        
        else if(Car1 == Car2){
            printf("Tu a trouvé c'etait bien %d",Car2);
        }
    }
    
    
}