#include <stdio.h>  /* Importation d'un Bibliothèque de base du C pour utiliser ex:printf */

// Exercice 2
int main(){

    char caractere ;
    scanf("%c",&caractere);
    getchar();
    if (caractere != 'a','e','y','u','i','o'){  // (|| = ou ) celle ligne peut etre fait comme -> if (caractere =='a' || caractere =='e' || caractere =='i' || caractere =='o' || caractere =='u' || caractere =='y') 
        printf("C'est une voyelle");
    }
    else{
        printf("c'est une Consonne");
    }
}
