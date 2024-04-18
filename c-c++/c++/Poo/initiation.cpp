#include <iostream>
using namespace std;

class Rectangle {
    public:
        double surface(){
            return Hauteur*Largeur;
        };
        double getHauteur(){
            return Hauteur;
        };
        double getLargeur(){
            return Largeur;
        };
        void setHauteur(double h){
            Largeur = h;
        };
        void setLargeur(double l){
            Largeur = l;
        };
    private :
        double Hauteur;
        double Largeur ;
};

int main(){
    Rectangle rect1;

    rect1.Hauteur(4.0) ;
    rect1.Largeur(5.0) ;

    cout << "Surface :" << rect1.surface() << " cm" << endl ;
    cout << "Hauteur :" << rect1.getHauteur() << " cm" << endl ;

    return 0;
};