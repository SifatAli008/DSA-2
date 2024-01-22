//digit extract
// Created by Sifat Ali on 1/9/2024.
//
#include <iostream>
using namespace std;

void digit(int n){
    if(n==0){
        return;
    }else{
        int lastvalue = n%10;
        digit(n/=10);
        cout<<lastvalue<<" ";
    }
}

int main(){
    int num;
    cout<<"Enter a Number : ";
    cin>>num;
    digit(num);
}