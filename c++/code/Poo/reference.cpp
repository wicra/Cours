
#include <iostream>
using namespace std;

int main(){
    int i ;
    int &r = i;
    r = 50;
    cout << r << " :" << i  << endl;
    return  0;
}


