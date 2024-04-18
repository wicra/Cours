#include<stdio.h>

// * c'est le contenue et & c'est lendroit
void inverser (int *a, int *b) {
int z;
z = *a;
*a = *b;
*b = z;
}

int main (void) {
int x=10;
int y=20;
printf ("x: %d\n y: %d \n", x,y) ;

inverser (&x,&y); // puis utiliser la fonction inverser pour inverser 
printf ("x: %d \n y: %d\n", x,y) ; // Puis afficher apres inversion

}