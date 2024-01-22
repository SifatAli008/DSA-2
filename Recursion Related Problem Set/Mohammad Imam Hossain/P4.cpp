//revese print;
// Created by Sifat Ali on 1/7/2024.
//
#include <iostream>
using namespace std;

void printRec(int n){
    if(n==0) {
        return;
    }
    else {
        cout << n<<" ";
        printRec(n - 1);
    }
}
int main(){
    int n;
    cin>>n;
    printRec(n);
}