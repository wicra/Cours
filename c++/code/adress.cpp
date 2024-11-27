#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    int _cidr;
    int ip[4], masque[4], adresseReseau[4], adresseDiffusion[4];
    
    // Demande de l'adresse IP
    cout << "Entrez l'adresse IP (exemple: 192.168.1.10) : ";
    // Convertir l'adresse IP en tableau d'octets
    scanf("%d.%d.%d.%d", &ip[0], &ip[1], &ip[2], &ip[3]);
    cout << endl;
    // Demande du masque de sous-réseau
    cout << "Entrez le masque de sous-réseau (exemple: 255.255.255.0) : ";
    // Convertir le masque en tableau d'octets
    scanf("%d.%d.%d.%d", &masque[0], &masque[1], &masque[2], &masque[3]);
    cout << endl;
    // Calcul de l'adresse réseau
    cout << "Adresse réseau : ";
    for (int i = 0; i < 4; i++) {
        adresseReseau[i] = ip[i] & masque[i];
        cout << adresseReseau[i];
        if (i < 3) {
            cout << ".";
        }
    }
    cout << endl;

    // Calcul de l'adresse de diffusion
    cout << "Adresse de diffusion : ";
    for (int i = 0; i < 4; i++) {
        adresseDiffusion[i] = ip[i] |masque[i];
        cout << adresseDiffusion[i];
        if (i < 3) {
            cout << ".";
        }
    }
    cout << endl;

    // CIDR
    cout << "\nEntrez le CIDR : ";
    cin >> _cidr;
    int i;
    if(_cidr<=32){
        for(i = 0; i < 4; i++){
            masque[i]=0;
        }
        i = 0;
        while (_cidr >= 8)
        {
            masque[i++] = 255;
            _cidr -= 8;
        }
        unsigned char puissance = 128;
        while (_cidr-- > 0)
        {
            masque[i] += puissance;
            puissance /= 2;
        }
        for (int i = 0; i<4; i++){
            cout << masque[i];
            if (i<3){
                cout << ".";
            }
        }
    }
    
    return 0;
}

