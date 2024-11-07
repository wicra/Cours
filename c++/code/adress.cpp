#include <iostream>
#include <cstdio>

using namespace std;

int main() {

    int ip[4], masque[4];

    // Demande de l'adresse IP
    cout << "Entrez l'adresse IP (exemple: 192.168.1.10) : ";
    cin >> ip;

    // Convertir l'adresse IP en tableau d'octets
    sscanf(adresseIp.c_str(), "%d.%d.%d.%d", &ip[0], &ip[1], &ip[2], &ip[3]);

    // Demande du masque de sous-réseau
    cout << "Entrez le masque de sous-réseau (exemple: 255.255.255.0) : ";
    cin >> masque;

    // Convertir le masque en tableau d'octets
    sscanf(adresseMasque.c_str(), "%d.%d.%d.%d", &masque[0], &masque[1], &masque[2], &masque[3]);

    // Calcul de l'adresse réseau et de l'adresse de broadcast
    for (int j = 0; j < 4; j++) {
        reseau[j] = ip[j] & masque[j];                 // Adresse réseau
        broadcast[j] = ip[j] | (~masque[j] & 0xFF);    // Adresse de broadcast
    }

    // Affichage de l'adresse réseau
    cout << "Adresse réseau : ";
    for (int j = 0; j < 4; j++) {
        cout << reseau[j];
        if (j < 3) cout << ".";
    }
    cout << endl;

    // Affichage de l'adresse de broadcast
    cout << "Adresse de broadcast : ";
    for (int j = 0; j < 4; j++) {
        cout << broadcast[j];
        if (j < 3) cout << ".";
    }
    cout << endl;


}
