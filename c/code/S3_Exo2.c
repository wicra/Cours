
#include <stdio.h>
#define NB_VAL 10

// Afficher 

int main(){

    int ligne;
    int colonne;
    for( ligne = 0; ligne < NB_VAL  ; ligne++){
       
        for(colonne = 0; colonne < NB_VAL ; colonne++){
            printf(" X");
        }
        printf("\n");
    }
    

}
