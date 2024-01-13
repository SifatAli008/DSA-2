//POWER
// Created by Sifat Ali on 1/12/2024.
//
#include <iostream>
using namespace std;

int pow(int base,int n){
    if(n==0) return 1;
    else return base* pow(base, n-1);
}

int main(){
    int base,n;
    cin>>base>>n;
   cout<<pow(base,n);
}