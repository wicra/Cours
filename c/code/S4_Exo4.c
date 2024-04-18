// DONNER VOTRE NIVEAU


#include <stdio.h>

int main(){

    printf("Voici les niveau \n 1- Exellent \n 2- Bon \n 3- Moyen \n 4- Mauvais \n 5- Horrible \n ");
    printf("Entrez votre niveau en C :");
    int niveau;
    scanf("%d",&niveau);
    getchar();

    switch (niveau)
    {
        case 1 : 
            printf("bin cv alors");
            break;
        case 2 : 
            printf("pas mal ");
            break;
        case 3 : 
            printf("bon ameliore toi juste un peut ");
            break;
        
        case 4 : 
            printf("faut que tu travaille plus");
            break;
        case 5 :
            printf("quitte le metier ");
            break;

        default :
            printf("même choisir un nombre entre 1 et 5 tu sais pas ");
            break ;
        

    }

}