//Decimal to binary
// Created by Sifat Ali on 1/9/2024.
//
#include <iostream>
using namespace std;

void DecimalToBinary(int n){
    if(n==0){
        return;
    }else{
        int rest=n/2;
        DecimalToBinary(rest);
        cout<<n%2;
    }
}


int main(){
    int num;
    cout<<"Enter a Number : ";
    cin>>num;
    DecimalToBinary(num);
}
