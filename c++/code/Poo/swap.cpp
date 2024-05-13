
#include <iostream>
using namespace std;


void swap(int a , int b){
    cout << "a = " << a << " - b= " << b << endl;
    int c = a;
    a = b;
    b = c;
    cout << "a = " << a << " - b= " << b << endl;
}

void swap(int *a , int *b){
    cout << "a = " << *a << " - b= " << *b << endl;
    int c = *a;
    *a = *b;
    *b = c;
    cout << "a = " << *a << " - b= " << *b << endl;
}


int main(){
    int first = 33 ;
    int second = 44;
    swap (&first , &second);
    cout << "first = " << first << " - second= " << second << endl;
    return  0;
}


