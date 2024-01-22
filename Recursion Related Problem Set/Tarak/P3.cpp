//Calculate the factorial of n.
// Created by Sifat Ali on 1/8/2024.
//
#include <iostream>
using namespace std;

int Factorial(int n){
    if(n==0||n==1){
        return 1;
    } else{
        return n*=Factorial(n-1);
    }
}


int main(){
    int n;
    cout<<"Enter a value : ";
    cin>>n;

    cout<<"Total : "<<Factorial(n);
}