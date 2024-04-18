
#include <stdio.h>
#include <stdlib.h>

// inverser le min et max si ce n'est pas le cas

void Echange(int *min, int *max){

int cade_vide ;
cade_vide = *min;
*min = *max;
*max = cade_vide;  

if (min < max){
    printf("%d est inférieur a %d",*min,*max);
}
else{
    
    printf("%d est inferieur a %d",*min,*max);
}

}

int main(void){

    int min;
    scanf("%d",&min);
    getchar();

    int max;
    scanf("%d",&max);
    getchar();

    Echange(&max , &min);

}