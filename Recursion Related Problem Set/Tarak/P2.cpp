//Calculate the sum of numbers from 1 to n.
// Created by Sifat Ali on 1/8/2024.
//
#include <iostream>
using namespace std;

int PrintN(int n){
    if(n==0){
        return 0;
    } else{
        return n+=PrintN(n-1);
    }
}

int main(){
    int n;
    cout<<"Enter a value : ";
    cin>>n;

    cout<<"Total : "<<PrintN(n);
}